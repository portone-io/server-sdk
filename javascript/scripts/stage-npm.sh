#!/usr/bin/env bash
set -euo pipefail

package=@portone/server-sdk
version=$(jq -er '.version' package.json)
stage_result="$RUNNER_TEMP/server-sdk-npm-stage.json"
rm -f "$stage_result"

# Only stable releases go through this workflow.
if [[ ! $version =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Skipping prerelease $package@$version"
  exit 0
fi

# Stage only on the push that changes the package version. A repeat push
# while the version awaits 2FA must not submit a second staging attempt.
# If staging actually failed or was rejected, verify it is no longer pending
# in npm before re-running the original version-bump workflow.
before=${RELEASE_BEFORE_SHA:?}
[[ $before =~ ^[0-9a-f]{40}$ ]]
if [[ $before != 0000000000000000000000000000000000000000 ]]; then
  git cat-file -e "$before^{commit}" 2>/dev/null || git fetch --no-tags --depth=1 origin "$before"
  previous_version=$(git show "$before:javascript/package.json" | jq -er '.version')
  if [[ $previous_version == "$version" ]]; then
    echo "No new stable version in this push"
    exit 0
  fi
fi

registry=https://registry.npmjs.org
versions=$(npm view "$package" versions --json --registry="$registry")
if jq -e --arg version "$version" 'index($version) != null' <<< "$versions" > /dev/null; then
  echo "$package@$version is already published"
  exit 0
fi

# Preserve the repository's js-vVERSION tag and never overwrite it.
tag="js-v$version"
head=$(git rev-parse HEAD)
remote_tags=$(git ls-remote origin "refs/tags/$tag" "refs/tags/$tag^{}")
remote_tag=$(awk '/\^\{\}$/ { peeled = $1; next } { tag = $1 } END { print (peeled == "" ? tag : peeled) }' <<< "$remote_tags")
if [[ -n $remote_tag && $remote_tag != "$head" ]]; then
  echo "$tag already points at a different commit" >&2
  exit 1
fi

local_tag=$(git rev-parse --verify "refs/tags/$tag^{commit}" 2>/dev/null || true)
if [[ -z $local_tag ]]; then
  git tag "$tag" "$head"
elif [[ $local_tag != "$head" ]]; then
  echo "$tag already points at a different local commit" >&2
  exit 1
fi

# The SDK build uses git describe to embed its release version.
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT
pnpm build
sed -i "s/VERSION_PLACEHOLDER/$version/" jsr.json
pnpm pack --pack-destination "$scratch"
tarballs=("$scratch"/*.tgz)
[[ ${#tarballs[@]} == 1 && -f ${tarballs[0]} ]]

# JSR remains an immediate publication. On retry, skip a version already
# published there, but do not suppress an authentication or network error.
jsr_versions=$(curl -fsSL "https://jsr.io/$package/meta.json")
if ! jq -e --arg version "$version" '.versions | has($version)' <<< "$jsr_versions" > /dev/null; then
  pnpm exec jsr publish --allow-dirty
fi

if [[ -z $remote_tag ]]; then
  # Checkout intentionally doesn't persist credentials.
  auth=$(printf 'x-access-token:%s' "$GITHUB_TOKEN" | base64 -w0)
  echo "::add-mask::$auth"
  GIT_CONFIG_COUNT=1 \
    GIT_CONFIG_KEY_0=http.https://github.com/.extraheader \
    GIT_CONFIG_VALUE_0="AUTHORIZATION: basic $auth" \
    git push origin "HEAD:refs/tags/$tag"
fi

# Use the repository-pinned pnpm to build the tarball, and a separate pinned
# npm CLI for the staging endpoint.
npm exec --registry="$registry" --yes --package=npm@12.2.3 -- npm stage publish "${tarballs[0]}" \
  --registry="$registry" --access=public --provenance --json > "$scratch/stage.json"
jq -e --arg package "$package" --arg version "$version" \
  '.[$package] | select(.version == $version and (.stageId | type == "string" and length > 0))' \
  "$scratch/stage.json" > "$stage_result"

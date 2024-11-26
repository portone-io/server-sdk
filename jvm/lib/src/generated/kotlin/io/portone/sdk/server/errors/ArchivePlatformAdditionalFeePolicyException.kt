package io.portone.sdk.server.errors

public sealed interface ArchivePlatformAdditionalFeePolicyException : PlatformPolicyException {
  public override val message: String?
}

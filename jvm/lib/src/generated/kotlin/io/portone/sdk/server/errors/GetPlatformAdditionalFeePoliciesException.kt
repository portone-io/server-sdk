package io.portone.sdk.server.errors

public sealed interface GetPlatformAdditionalFeePoliciesException : PlatformPolicyException {
  public override val message: String?
}

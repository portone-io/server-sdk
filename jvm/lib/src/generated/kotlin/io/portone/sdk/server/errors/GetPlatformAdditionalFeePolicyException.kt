package io.portone.sdk.server.errors

public sealed interface GetPlatformAdditionalFeePolicyException : PlatformPolicyException {
  public override val message: String?
}

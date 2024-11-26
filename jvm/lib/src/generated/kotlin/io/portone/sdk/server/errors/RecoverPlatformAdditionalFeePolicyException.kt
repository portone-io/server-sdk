package io.portone.sdk.server.errors

public sealed interface RecoverPlatformAdditionalFeePolicyException : PlatformPolicyException {
  public override val message: String?
}

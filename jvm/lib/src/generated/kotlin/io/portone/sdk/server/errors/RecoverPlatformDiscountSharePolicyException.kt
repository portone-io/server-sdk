package io.portone.sdk.server.errors

public sealed interface RecoverPlatformDiscountSharePolicyException : PlatformPolicyException {
  public override val message: String?
}

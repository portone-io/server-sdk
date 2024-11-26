package io.portone.sdk.server.errors

public sealed interface UpdatePlatformDiscountSharePolicyException : PlatformPolicyException {
  public override val message: String?
}

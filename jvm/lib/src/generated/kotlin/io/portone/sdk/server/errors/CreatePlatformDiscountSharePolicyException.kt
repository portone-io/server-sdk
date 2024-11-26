package io.portone.sdk.server.errors

public sealed interface CreatePlatformDiscountSharePolicyException : PlatformPolicyException {
  public override val message: String?
}

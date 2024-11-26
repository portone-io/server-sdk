package io.portone.sdk.server.errors

public sealed interface GetPlatformDiscountSharePolicyException : PlatformPolicyException {
  public override val message: String?
}

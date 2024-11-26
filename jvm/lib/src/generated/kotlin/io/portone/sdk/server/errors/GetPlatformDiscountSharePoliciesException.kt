package io.portone.sdk.server.errors

public sealed interface GetPlatformDiscountSharePoliciesException : PlatformPolicyException {
  public override val message: String?
}

package io.portone.sdk.server.errors

public sealed interface RescheduleDiscountSharePolicyException : PlatformException {
  public override val message: String?
}

package io.portone.sdk.server.errors

public sealed interface ScheduleDiscountSharePolicyException : PlatformException {
  public override val message: String?
}
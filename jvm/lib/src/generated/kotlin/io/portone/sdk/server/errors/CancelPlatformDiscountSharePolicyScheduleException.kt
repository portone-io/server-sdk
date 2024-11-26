package io.portone.sdk.server.errors

public sealed interface CancelPlatformDiscountSharePolicyScheduleException : PlatformException {
  public override val message: String?
}

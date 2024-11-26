package io.portone.sdk.server.errors

public sealed interface ScheduleAdditionalFeePolicyException : PlatformException {
  public override val message: String?
}

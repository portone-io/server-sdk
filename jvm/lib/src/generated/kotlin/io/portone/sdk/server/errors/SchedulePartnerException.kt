package io.portone.sdk.server.errors

public sealed interface SchedulePartnerException : PlatformException {
  public override val message: String?
}

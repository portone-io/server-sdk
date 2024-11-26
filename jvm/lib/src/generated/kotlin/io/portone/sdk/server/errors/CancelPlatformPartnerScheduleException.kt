package io.portone.sdk.server.errors

public sealed interface CancelPlatformPartnerScheduleException : PlatformException {
  public override val message: String?
}

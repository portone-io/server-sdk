package io.portone.sdk.server.errors

public sealed interface GetPlatformPartnerScheduleException : PlatformException {
  public override val message: String?
}

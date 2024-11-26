package io.portone.sdk.server.errors

public sealed interface SchedulePlatformPartnersException : PlatformException {
  public override val message: String?
}

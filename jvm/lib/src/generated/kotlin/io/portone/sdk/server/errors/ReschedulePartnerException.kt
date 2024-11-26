package io.portone.sdk.server.errors

public sealed interface ReschedulePartnerException : PlatformException {
  public override val message: String?
}

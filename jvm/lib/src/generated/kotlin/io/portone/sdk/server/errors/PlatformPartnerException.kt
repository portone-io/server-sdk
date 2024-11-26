package io.portone.sdk.server.errors

public sealed interface PlatformPartnerException : PlatformException {
  public override val message: String?
}

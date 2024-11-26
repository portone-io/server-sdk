package io.portone.sdk.server.errors

public sealed interface GetPlatformPartnersException : PlatformPartnerException {
  public override val message: String?
}

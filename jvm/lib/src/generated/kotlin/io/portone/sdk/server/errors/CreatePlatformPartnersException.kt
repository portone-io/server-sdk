package io.portone.sdk.server.errors

public sealed interface CreatePlatformPartnersException : PlatformPartnerException {
  public override val message: String?
}

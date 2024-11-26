package io.portone.sdk.server.errors

public sealed interface CreatePlatformPartnerException : PlatformPartnerException {
  public override val message: String?
}

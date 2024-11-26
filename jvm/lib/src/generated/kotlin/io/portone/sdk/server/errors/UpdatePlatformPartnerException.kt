package io.portone.sdk.server.errors

public sealed interface UpdatePlatformPartnerException : PlatformPartnerException {
  public override val message: String?
}

package io.portone.sdk.server.errors

public sealed interface GetPlatformPartnerException : PlatformPartnerException {
  public override val message: String?
}

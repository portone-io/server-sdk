package io.portone.sdk.server.errors

public sealed interface RecoverPlatformPartnerException : PlatformPartnerException {
  public override val message: String?
}

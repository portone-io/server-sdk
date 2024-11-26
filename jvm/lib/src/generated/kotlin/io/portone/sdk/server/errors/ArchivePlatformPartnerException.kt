package io.portone.sdk.server.errors

public sealed interface ArchivePlatformPartnerException : PlatformPartnerException {
  public override val message: String?
}

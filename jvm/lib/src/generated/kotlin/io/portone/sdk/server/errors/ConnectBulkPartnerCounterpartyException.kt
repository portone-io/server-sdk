package io.portone.sdk.server.errors

public sealed interface ConnectBulkPartnerCounterpartyException : PlatformPartnerException {
  public override val message: String?
}

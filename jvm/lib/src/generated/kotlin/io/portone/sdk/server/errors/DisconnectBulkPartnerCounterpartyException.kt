package io.portone.sdk.server.errors

public sealed interface DisconnectBulkPartnerCounterpartyException : PlatformPartnerException {
  public override val message: String?
}

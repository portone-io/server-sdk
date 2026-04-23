package io.portone.sdk.server.errors

public sealed interface DisconnectPartnerCounterpartyException : PlatformPartnerException {
  public override val message: String?
}

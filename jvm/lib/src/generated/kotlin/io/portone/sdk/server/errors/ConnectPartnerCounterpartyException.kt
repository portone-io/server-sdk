package io.portone.sdk.server.errors

public sealed interface ConnectPartnerCounterpartyException : PlatformPartnerException {
  public override val message: String?
}

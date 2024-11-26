package io.portone.sdk.server.errors

public sealed interface PlatformPartnerSettlementException : PlatformException {
  public override val message: String?
}

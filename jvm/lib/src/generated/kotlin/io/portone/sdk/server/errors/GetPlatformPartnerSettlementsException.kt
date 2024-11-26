package io.portone.sdk.server.errors

public sealed interface GetPlatformPartnerSettlementsException : PlatformPartnerSettlementException {
  public override val message: String?
}

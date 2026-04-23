package io.portone.sdk.server.errors

public sealed interface DeletePlatformPartnerSettlementsException : PlatformPartnerSettlementException {
  public override val message: String?
}

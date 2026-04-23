package io.portone.sdk.server.errors

public sealed interface CompletePlatformPayoutByPartnerSettlementIdsException : PlatformPayoutException {
  public override val message: String?
}

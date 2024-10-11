package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError
import java.lang.Exception


/** 정산 요청 공급대가가 포트원 결제 내역의 공급대가를 초과한 경우 */
public class PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentException(
  cause: PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError
) : Exception(cause.message) {
  public val registeredSettlementSupplyWithVatAmount: Long = cause.registeredSettlementSupplyWithVatAmount,
  public val requestSettlementSupplyWithVatAmount: Long = cause.requestSettlementSupplyWithVatAmount,
  public val portOneSupplyWithVatAmount: Long = cause.portOneSupplyWithVatAmount,
}

package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformSettlementTaxFreeAmountExceededPortOnePaymentError
import java.lang.Exception


/** 정산 요청 면세 금액이 포트원 결제 내역의 면세 금액을 초과한 경우 */
public class PlatformSettlementTaxFreeAmountExceededPortOnePaymentException(
  cause: PlatformSettlementTaxFreeAmountExceededPortOnePaymentError
) : Exception(cause.message) {
  public val registeredSettlementTaxFreeAmount: Long = cause.registeredSettlementTaxFreeAmount,
  public val requestSettlementTaxFreeAmount: Long = cause.requestSettlementTaxFreeAmount,
  public val portOneTaxFreeAmount: Long = cause.portOneTaxFreeAmount,
}

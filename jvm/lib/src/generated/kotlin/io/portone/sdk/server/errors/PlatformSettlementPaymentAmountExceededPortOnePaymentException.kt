package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformSettlementPaymentAmountExceededPortOnePaymentError
import java.lang.Exception


/** 정산 요청 결제 금액이 포트원 결제 내역의 결제 금액을 초과한 경우 */
public class PlatformSettlementPaymentAmountExceededPortOnePaymentException internal constructor(
  cause: PlatformSettlementPaymentAmountExceededPortOnePaymentError
) : PortOneException(cause.message), CreatePlatformOrderTransferException {
  public val registeredSettlementPaymentAmount: Long = cause.registeredSettlementPaymentAmount
  public val requestSettlementPaymentAmount: Long = cause.requestSettlementPaymentAmount
  public val portOnePaymentAmount: Long = cause.portOnePaymentAmount
}

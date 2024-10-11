package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformPortOnePaymentCancelAmountType
import io.portone.sdk.server.platform.transfer.PlatformSettlementCancelAmountExceededPortOneCancelError
import java.lang.Exception


/** 정산 취소 요청 금액이 포트원 결제 취소 내역의 취소 금액을 초과한 경우 */
public class PlatformSettlementCancelAmountExceededPortOneCancelException(
  cause: PlatformSettlementCancelAmountExceededPortOneCancelError
) : Exception(cause.message) {
  public val registeredSettlementCancelAmount: Long = cause.registeredSettlementCancelAmount,
  public val requestSettlementCancelAmount: Long = cause.requestSettlementCancelAmount,
  public val portOneCancelAmount: Long = cause.portOneCancelAmount,
  public val amountType: PlatformPortOnePaymentCancelAmountType = cause.amountType,
}

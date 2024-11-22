package io.portone.sdk.server.payment.cashreceipt

import io.portone.sdk.server.payment.cashreceipt.CashReceiptSummary
import kotlinx.serialization.Serializable

/** 현금 영수증 발급 성공 응답 */
@Serializable
public data class IssueCashReceiptResponse(
  val cashReceipt: CashReceiptSummary,
)



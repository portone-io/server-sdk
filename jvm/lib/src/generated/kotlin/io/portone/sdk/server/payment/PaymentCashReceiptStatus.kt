package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 결제건 내 현금영수증 상태 */
@Serializable
public enum class PaymentCashReceiptStatus {
  Issued,
  Cancelled,
}

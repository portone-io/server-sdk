package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 웹훅 발송 시 결제 건 상태 */
@Serializable
public enum class PaymentWebhookPaymentStatus {
  READY,
  VIRTUAL_ACCOUNT_ISSUED,
  PAID,
  FAILED,
  PARTIAL_CANCELLED,
  CANCELLED,
  PAY_PENDING,
}

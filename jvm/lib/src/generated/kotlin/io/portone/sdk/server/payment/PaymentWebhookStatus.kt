package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 웹훅 전송 상태 */
@Serializable
public enum class PaymentWebhookStatus {
  SUCCEEDED,
  FAILED_NOT_OK_RESPONSE,
  FAILED_UNEXPECTED_ERROR,
}

package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 웹훅 전송 상태 */
@Serializable
public enum class PaymentWebhookStatus {
  Succeeded,
  FailedNotOkResponse,
  FailedUnexpectedError,
}

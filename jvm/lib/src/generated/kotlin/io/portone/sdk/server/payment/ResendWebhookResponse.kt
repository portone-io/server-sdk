package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentWebhook
import kotlinx.serialization.Serializable

/** 웹훅 재발송 응답 정보 */
@Serializable
public data class ResendWebhookResponse(
  /** 재발송 웹훅 정보 */
  val webhook: PaymentWebhook,
)

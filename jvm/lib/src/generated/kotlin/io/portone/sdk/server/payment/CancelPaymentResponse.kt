package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentCancellation
import kotlinx.serialization.Serializable

/** 결제 취소 성공 응답 */
@Serializable
public data class CancelPaymentResponse(
  /** 결제 취소 내역 */
  val cancellation: PaymentCancellation,
)



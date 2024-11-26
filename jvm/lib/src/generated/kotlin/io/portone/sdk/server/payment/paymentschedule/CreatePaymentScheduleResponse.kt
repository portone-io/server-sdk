package io.portone.sdk.server.payment.paymentschedule

import io.portone.sdk.server.payment.paymentschedule.PaymentScheduleSummary
import kotlinx.serialization.Serializable

/** 결제 예약 성공 응답 */
@Serializable
public data class CreatePaymentScheduleResponse(
  /** 결제 예약 건 */
  val schedule: PaymentScheduleSummary,
)



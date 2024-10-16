package io.portone.sdk.server.payment.paymentschedule

import io.portone.sdk.server.common.BillingKeyPaymentInput
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlinx.serialization.Serializable

/** 결제 예약 요청 입력 정보 */
@Serializable
internal data class CreatePaymentScheduleBody(
  /** 빌링키 결제 입력 정보 */
  val payment: BillingKeyPaymentInput,
  /** 결제 예정 시점 */
  val timeToPay: @Serializable(InstantSerializer::class) Instant,
)

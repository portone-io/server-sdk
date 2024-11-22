package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.BillingKeyPaymentSummary
import kotlinx.serialization.Serializable

/** 빌링키 결제 성공 응답 */
@Serializable
public data class PayWithBillingKeyResponse(
  /** 결제 건 요약 정보 */
  val payment: BillingKeyPaymentSummary,
)



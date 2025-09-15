package io.portone.sdk.server.payment.billingkey

import kotlin.String
import kotlinx.serialization.Serializable

/** 빌링키 발급 및 초회 결제 수동 승인 완료 응답 */
@Serializable
public data class ConfirmedBillingKeyIssueAndPaySummary(
  /** 빌링키 */
  val billingKey: String,
  /** 결제 건 아이디 */
  val paymentId: String,
)



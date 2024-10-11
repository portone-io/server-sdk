package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 빌링키 결제 완료된 결제 건 요약 정보 */
@Serializable
public data class BillingKeyPaymentSummary(
  /** PG사 결제 아이디 */
  val pgTxId: String,
  /** 결제 완료 시점 */
  val paidAt: Instant,
)

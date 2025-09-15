package io.portone.sdk.server.payment.billingkey

import kotlin.String
import kotlinx.serialization.Serializable

/** 빌링키 발급 수동 승인 완료 응답 */
@Serializable
public data class ConfirmedBillingKeySummary(
  /** 빌링키 */
  val billingKey: String,
)



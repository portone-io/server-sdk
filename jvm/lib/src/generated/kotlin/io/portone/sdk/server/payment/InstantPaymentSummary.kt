package io.portone.sdk.server.payment

import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 수기 결제가 완료된 결제 건 요약 정보 */
@Serializable
public data class InstantPaymentSummary(
  /** PG사 결제 아이디 */
  val pgTxId: String,
  /** 결제 완료 시점 */
  val paidAt: Instant,
)

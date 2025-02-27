package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.DisputeStatus
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 분쟁 내역 */
@Serializable
public data class Dispute(
  /** 분쟁 상태 */
  val status: DisputeStatus,
  /** PG사 분쟁 아이디 */
  val pgDisputeId: String? = null,
  /** 분쟁 사유 */
  val reason: String,
  /** 분쟁 발생 시각 */
  val createdAt: @Serializable(InstantSerializer::class) Instant,
  /** 분쟁 해소 시각 */
  val resolvedAt: @Serializable(InstantSerializer::class) Instant? = null,
)



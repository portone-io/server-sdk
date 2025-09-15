package io.portone.sdk.server.platform.payout

import io.portone.sdk.server.platform.payout.PlatformPayoutSettlementStatementStatus
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 정산 내역서 요약 정보 */
@Serializable
public data class PlatformPayoutSettlementStatementSummary(
  /** 상태 */
  val status: PlatformPayoutSettlementStatementStatus,
  /** 아이디 */
  val id: String? = null,
  /** 발송 일시 */
  val issuedAt: @Serializable(InstantSerializer::class) Instant? = null,
)



package io.portone.sdk.server.platform.bulkpayout

import io.portone.sdk.server.platform.PlatformPayoutMethod
import io.portone.sdk.server.platform.bulkpayout.PlatformBulkPayoutStats
import io.portone.sdk.server.platform.bulkpayout.PlatformBulkPayoutStatus
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkPayout(
  /** 일괄 지급 고유 아이디 */
  val id: String,
  val graphqlId: String,
  /** 이름 */
  val name: String,
  /** 생성자 아이디 */
  val creatorId: String,
  /** 지급 유형 */
  val method: PlatformPayoutMethod,
  /** 총 지급 금액 */
  val totalPayoutAmount: Long,
  /** 총 정산 금액 */
  val totalSettlementAmount: Long,
  /** 상태 */
  val status: PlatformBulkPayoutStatus,
  /** 지급 통계 */
  val payoutStats: PlatformBulkPayoutStats,
  /** 상태 업데이트 일시 */
  val statusUpdatedAt: @Serializable(InstantSerializer::class) Instant,
  /** 생성 일시 */
  val createdAt: @Serializable(InstantSerializer::class) Instant,
  /** 업데이트 일시 */
  val updatedAt: @Serializable(InstantSerializer::class) Instant,
)



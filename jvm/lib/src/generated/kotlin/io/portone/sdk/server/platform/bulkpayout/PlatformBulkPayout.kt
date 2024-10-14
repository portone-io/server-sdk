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
  val name: String,
  val creatorId: String,
  val method: PlatformPayoutMethod,
  val arePayoutsGenerated: Boolean,
  val totalPayoutAmount: Long,
  val status: PlatformBulkPayoutStatus,
  val payoutStats: PlatformBulkPayoutStats,
  val statusUpdatedAt: @Serializable(InstantSerializer::class) Instant,
  val createdAt: @Serializable(InstantSerializer::class) Instant,
  val updatedAt: @Serializable(InstantSerializer::class) Instant,
  val scheduledAt: @Serializable(InstantSerializer::class) Instant? = null,
)

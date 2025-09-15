package io.portone.sdk.server.platform.bulkaccounttransfer

import io.portone.sdk.server.platform.bulkaccounttransfer.PlatformBulkAccountTransferStats
import io.portone.sdk.server.platform.bulkaccounttransfer.PlatformBulkAccountTransferStatus
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkAccountTransfer(
  /** 일괄 이체 고유 아이디 */
  val id: String,
  val graphqlId: String,
  val creatorId: String,
  /** 출금 계좌 아이디 */
  val bankAccountId: String,
  val bankAccountGraphqlId: String,
  val totalAmount: Long,
  val status: PlatformBulkAccountTransferStatus,
  val stats: PlatformBulkAccountTransferStats,
  val statusUpdatedAt: @Serializable(InstantSerializer::class) Instant,
  val createdAt: @Serializable(InstantSerializer::class) Instant,
  val updatedAt: @Serializable(InstantSerializer::class) Instant,
  val scheduledAt: @Serializable(InstantSerializer::class) Instant? = null,
)



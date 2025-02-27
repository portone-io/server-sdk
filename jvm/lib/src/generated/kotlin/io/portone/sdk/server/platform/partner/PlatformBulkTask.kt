package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.partner.PlatformBulkTaskProgressStats
import io.portone.sdk.server.platform.partner.PlatformBulkTaskStatus
import io.portone.sdk.server.platform.partner.PlatformBulkTaskType
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkTask(
  val id: String,
  val graphqlId: String,
  val status: PlatformBulkTaskStatus,
  val type: PlatformBulkTaskType,
  val progressStats: PlatformBulkTaskProgressStats,
  val isForTest: Boolean,
  val statusUpdatedAt: @Serializable(InstantSerializer::class) Instant,
  val createdAt: @Serializable(InstantSerializer::class) Instant,
  val updatedAt: @Serializable(InstantSerializer::class) Instant,
)



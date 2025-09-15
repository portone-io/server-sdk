package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

@Serializable
public data class PlatformPayoutStatusStats(
  val confirmed: Long,
  val prepared: Long,
  val cancelled: Long,
  val stopped: Long,
  val processing: Long,
  val succeeded: Long,
  val failed: Long,
  val scheduled: Long,
)



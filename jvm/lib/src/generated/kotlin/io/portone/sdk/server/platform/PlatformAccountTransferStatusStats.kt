package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

@Serializable
public data class PlatformAccountTransferStatusStats(
  val prepared: Long,
  val scheduled: Long,
  val cancelled: Long,
  val stopped: Long,
  val processing: Long,
  val asyncProcessing: Long,
  val succeeded: Long,
  val failed: Long,
)



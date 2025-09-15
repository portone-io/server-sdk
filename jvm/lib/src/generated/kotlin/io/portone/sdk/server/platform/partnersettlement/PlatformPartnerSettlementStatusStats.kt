package io.portone.sdk.server.platform.partnersettlement

import kotlinx.serialization.Serializable

@Serializable
public data class PlatformPartnerSettlementStatusStats(
  val payoutScheduled: Long,
  val payoutPrepared: Long,
  val payoutWithheld: Long,
  val payoutFailed: Long,
  val payoutCancelled: Long,
  val payoutConfirmed: Long,
  val inPayout: Long,
  val paidOut: Long,
)



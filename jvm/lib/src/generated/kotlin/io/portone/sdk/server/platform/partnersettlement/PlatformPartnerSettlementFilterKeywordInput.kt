package io.portone.sdk.server.platform.partnersettlement

import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformPartnerSettlementFilterKeywordInput(
  val partnerSettlementId: String? = null,
  val payoutId: String? = null,
  val bulkPayoutId: String? = null,
)

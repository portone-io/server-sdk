package io.portone.sdk.server.platform.payout

import kotlin.String
import kotlinx.serialization.Serializable

/** 일괄 지급 완료 처리 결과 */
@Serializable
public data class CompletePlatformPayoutByPartnerSettlementIdsResponse(
  val bulkPayoutId: String? = null,
  val bulkPayoutGraphqlId: String? = null,
  val payoutCount: Int,
  val partnerSettlementCount: Int,
)



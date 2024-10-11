package io.portone.sdk.server.platform.partnersettlement

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.partnersettlement.PlatformPartnerSettlementFilterKeywordInput
import io.portone.sdk.server.platform.partnersettlement.PlatformPartnerSettlementStatus
import io.portone.sdk.server.platform.partnersettlement.PlatformPartnerSettlementType
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformPartnerSettlementFilterInput(
  val settlementDates: List<String>? = null,
  val contractIds: List<String>? = null,
  val partnerTags: List<String>? = null,
  /** 통화 단위 */
  val settlementCurrencies: List<Currency>? = null,
  /** 정산 상태 */
  val statuses: List<PlatformPartnerSettlementStatus>? = null,
  val partnerIds: List<String>? = null,
  /** 정산 유형 */
  val settlementTypes: List<PlatformPartnerSettlementType>? = null,
  val keyword: PlatformPartnerSettlementFilterKeywordInput? = null,
)

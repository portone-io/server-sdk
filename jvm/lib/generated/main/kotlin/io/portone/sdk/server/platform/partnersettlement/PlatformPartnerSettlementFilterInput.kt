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
  val settlementDates: Array<String>? = null,
  val contractIds: Array<String>? = null,
  val partnerTags: Array<String>? = null,
  /** 통화 단위 */
  val settlementCurrencies: Array<Currency>? = null,
  /** 정산 상태 */
  val statuses: Array<PlatformPartnerSettlementStatus>? = null,
  val partnerIds: Array<String>? = null,
  /** 정산 유형 */
  val settlementTypes: Array<PlatformPartnerSettlementType>? = null,
  val keyword: PlatformPartnerSettlementFilterKeywordInput? = null,
)

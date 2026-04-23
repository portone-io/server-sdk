package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 지급 금액의 총합이 음수인 파트너가 존재하는 경우 */
@Serializable
@SerialName("PLATFORM_CURRENCY_NOT_SUPPORTED")
internal data class PlatformNegativePayoutAmountPartnersError(
  override val message: String? = null,
) : CompletePlatformPayoutByPartnerSettlementIdsError.Recognized



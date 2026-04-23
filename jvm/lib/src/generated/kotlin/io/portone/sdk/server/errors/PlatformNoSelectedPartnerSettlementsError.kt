package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 선택된 정산건이 없는 경우 */
@Serializable
@SerialName("PLATFORM_NO_SELECTED_PARTNER_SETTLEMENTS")
internal data class PlatformNoSelectedPartnerSettlementsError(
  override val message: String? = null,
) : CompletePlatformPayoutByPartnerSettlementIdsError.Recognized



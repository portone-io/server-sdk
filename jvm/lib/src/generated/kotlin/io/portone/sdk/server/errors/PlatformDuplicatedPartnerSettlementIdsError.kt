package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 선택된 정산건 아이디에 중복이 있는 경우 */
@Serializable
@SerialName("PLATFORM_DUPLICATED_PARTNER_SETTLEMENT_IDS")
internal data class PlatformDuplicatedPartnerSettlementIdsError(
  override val message: String? = null,
) : CompletePlatformPayoutByPartnerSettlementIdsError.Recognized



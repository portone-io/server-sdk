package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 일괄 지급 아이디가 이미 존재하는 경우 */
@Serializable
@SerialName("PLATFORM_BULK_PAYOUT_ID_ALREADY_EXISTS")
internal data class PlatformBulkPayoutIdAlreadyExistsError(
  override val message: String? = null,
) : CompletePlatformPayoutByPartnerSettlementIdsError.Recognized



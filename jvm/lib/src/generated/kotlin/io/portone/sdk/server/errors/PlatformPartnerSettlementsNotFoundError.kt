package io.portone.sdk.server.errors

import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 요청한 정산건 목록을 찾을 수 없는 경우 */
@Serializable
@SerialName("PLATFORM_PARTNER_SETTLEMENTS_NOT_FOUND")
internal data class PlatformPartnerSettlementsNotFoundError(
  val ids: List<String>,
  val graphqlIds: List<String>,
  override val message: String? = null,
) : CompletePlatformPayoutByPartnerSettlementIdsError.Recognized, DeletePlatformPartnerSettlementsError.Recognized



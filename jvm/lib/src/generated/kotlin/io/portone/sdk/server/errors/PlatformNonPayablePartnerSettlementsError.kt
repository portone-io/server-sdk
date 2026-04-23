package io.portone.sdk.server.errors

import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 지급할 수 없는 정산건이 포함된 경우 */
@Serializable
@SerialName("PLATFORM_NON_PAYABLE_PARTNER_SETTLEMENTS")
internal data class PlatformNonPayablePartnerSettlementsError(
  val ids: List<String>,
  val graphqlIds: List<String>,
  override val message: String? = null,
) : CompletePlatformPayoutByPartnerSettlementIdsError.Recognized



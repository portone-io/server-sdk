package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너 유형이 사업자가 아닌 경우 */
@Serializable
@SerialName("PLATFORM_PARTNER_TYPE_IS_NOT_BUSINESS")
internal data class PlatformPartnerTypeIsNotBusinessError(
  override val message: String? = null,
) : ConnectPartnerMemberCompanyError.Recognized, DisconnectPartnerMemberCompanyError.Recognized



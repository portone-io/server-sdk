package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너의 과세 유형이 간이 과세 세금계산서 미발행 유형인 경우 */
@Serializable
@SerialName("PLATFORM_PARTNER_TAXATION_TYPE_IS_SIMPLE")
internal data class PlatformPartnerTaxationTypeIsSimpleError(
  override val message: String? = null,
) : ConnectPartnerMemberCompanyError.Recognized, DisconnectPartnerMemberCompanyError.Recognized



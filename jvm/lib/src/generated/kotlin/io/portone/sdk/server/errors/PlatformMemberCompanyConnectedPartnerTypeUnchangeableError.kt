package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 연동 사업자로 연동된 파트너의 파트너 유형을 변경하려고 시도한 경우 */
@Serializable
@SerialName("PLATFORM_MEMBER_COMPANY_CONNECTED_PARTNER_TYPE_UNCHANGEABLE")
internal data class PlatformMemberCompanyConnectedPartnerTypeUnchangeableError(
  override val message: String? = null,
) : SchedulePartnerError.Recognized, UpdatePlatformPartnerError.Recognized



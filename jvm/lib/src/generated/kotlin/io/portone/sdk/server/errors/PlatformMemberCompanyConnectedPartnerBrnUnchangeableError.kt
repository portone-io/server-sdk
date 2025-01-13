package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 연동 사업자로 연동된 파트너의 사업자등록번호를 변경하려고 시도한 경우 */
@Serializable
@SerialName("PLATFORM_MEMBER_COMPANY_CONNECTED_PARTNER_BRN_UNCHANGEABLE")
internal data class PlatformMemberCompanyConnectedPartnerBrnUnchangeableError(
  override val message: String? = null,
) : SchedulePartnerError.Recognized, UpdatePlatformPartnerError.Recognized



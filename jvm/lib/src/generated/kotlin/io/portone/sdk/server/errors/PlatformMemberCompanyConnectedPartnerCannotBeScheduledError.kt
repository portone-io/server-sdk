package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 연동 사업자로 연동된 파트너를 예약 수정하려고 시도한 경우 */
@Serializable
@SerialName("PLATFORM_MEMBER_COMPANY_CONNECTED_PARTNER_CANNOT_BE_SCHEDULED")
internal data class PlatformMemberCompanyConnectedPartnerCannotBeScheduledError(
  override val message: String? = null,
) : ReschedulePartnerError.Recognized, SchedulePartnerError.Recognized



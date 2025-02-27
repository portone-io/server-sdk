package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너 수정 예약 건이 존재하는 경우 */
@Serializable
@SerialName("PLATFORM_PARTNER_SCHEDULE_EXISTS")
internal data class PlatformPartnerScheduleExistsError(
  override val message: String? = null,
) : ConnectPartnerMemberCompanyError.Recognized



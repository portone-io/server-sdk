package io.portone.sdk.server.errors

import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 연동 사업자로 연동된 파트너들을 예약 수정하려고 시도한 경우 */
@Serializable
@SerialName("PLATFORM_MEMBER_COMPANY_CONNECTED_PARTNERS_CANNOT_BE_SCHEDULED")
internal data class PlatformMemberCompanyConnectedPartnersCannotBeScheduledError(
  val ids: List<String>,
  val graphqlIds: List<String>,
  override val message: String? = null,
) : SchedulePlatformPartnersError.Recognized



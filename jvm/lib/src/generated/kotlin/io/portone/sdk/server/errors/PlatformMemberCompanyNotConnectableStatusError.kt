package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너 연동 사업자 연동 상태가 연동 가능한 상태가 아닌 경우 */
@Serializable
@SerialName("PLATFORM_MEMBER_COMPANY_NOT_CONNECTABLE_STATUS")
internal data class PlatformMemberCompanyNotConnectableStatusError(
  override val message: String? = null,
) : ConnectPartnerMemberCompanyError.Recognized



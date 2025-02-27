package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너가 연동 사업자로 연동 되어있지 않은 경우 */
@Serializable
@SerialName("PLATFORM_MEMBER_COMPANY_NOT_CONNECTED")
internal data class PlatformMemberCompanyNotConnectedError(
  override val message: String? = null,
) : DisconnectPartnerMemberCompanyError.Recognized



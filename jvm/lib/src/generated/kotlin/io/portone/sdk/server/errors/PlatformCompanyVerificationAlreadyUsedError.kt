package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너 사업자 검증 아이디를 이미 사용한 경우 */
@Serializable
@SerialName("PLATFORM_COMPANY_VERIFICATION_ALREADY_USED")
internal data class PlatformCompanyVerificationAlreadyUsedError(
  override val message: String? = null,
) : CreatePlatformPartnerError.Recognized, SchedulePartnerError.Recognized, UpdatePlatformPartnerError.Recognized



package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너 계좌 검증 아이디를 찾을 수 없는 경우 */
@Serializable
@SerialName("PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND")
internal data class PlatformAccountVerificationNotFoundError(
  override val message: String? = null,
) : CreatePlatformPartnerError.Recognized, SchedulePartnerError.Recognized, UpdatePlatformPartnerError.Recognized



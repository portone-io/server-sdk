package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너 계좌 인증이 실패한 경우 */
@Serializable
@SerialName("PLATFORM_ACCOUNT_VERIFICATION_FAILED")
internal data class PlatformAccountVerificationFailedError(
  override val message: String? = null,
) : CreatePlatformPartnerError.Recognized, SchedulePartnerError.Recognized, UpdatePlatformPartnerError.Recognized

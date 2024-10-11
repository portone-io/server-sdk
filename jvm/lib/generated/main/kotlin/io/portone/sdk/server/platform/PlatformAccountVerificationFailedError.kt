package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너 계좌 인증이 실패한 경우 */
@Serializable
@SerialName("PLATFORM_ACCOUNT_VERIFICATION_FAILED")
public data class PlatformAccountVerificationFailedError(
  override val message: String? = null,
): CreatePlatformPartnerError,
  ): SchedulePartnerError,
    ): UpdatePlatformPartnerError,

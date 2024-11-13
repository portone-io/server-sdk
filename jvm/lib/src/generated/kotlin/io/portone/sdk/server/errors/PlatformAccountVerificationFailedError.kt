package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너 계좌 인증이 실패한 경우 */
@Serializable
@SerialName("PLATFORM_ACCOUNT_VERIFICATION_FAILED")
@ConsistentCopyVisibility
public data class PlatformAccountVerificationFailedError internal constructor(
  val message: String? = null,
) : CreatePlatformPartnerError, SchedulePartnerError, UpdatePlatformPartnerError

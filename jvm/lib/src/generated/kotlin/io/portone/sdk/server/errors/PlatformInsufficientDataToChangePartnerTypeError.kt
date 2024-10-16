package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.SchedulePartnerError
import io.portone.sdk.server.errors.UpdatePlatformPartnerError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너 타입 수정에 필요한 데이터가 부족한 경우 */
@Serializable
@SerialName("PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE")
@ConsistentCopyVisibility
public data class PlatformInsufficientDataToChangePartnerTypeError internal constructor(
  override val message: String? = null,
): SchedulePartnerError,
  UpdatePlatformPartnerError

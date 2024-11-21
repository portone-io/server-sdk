package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 보관된 추가 수수료 정책을 업데이트하려고 하는 경우 */
@Serializable
@SerialName("PLATFORM_ARCHIVED_ADDITIONAL_FEE_POLICY")
internal data class PlatformArchivedAdditionalFeePolicyError(
  override val message: String? = null,
) : ScheduleAdditionalFeePolicyError.Recognized, UpdatePlatformAdditionalFeePolicyError.Recognized

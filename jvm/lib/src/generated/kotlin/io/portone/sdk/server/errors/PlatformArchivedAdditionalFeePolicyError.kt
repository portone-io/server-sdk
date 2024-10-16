package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ScheduleAdditionalFeePolicyError
import io.portone.sdk.server.errors.UpdatePlatformAdditionalFeePolicyError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 보관된 추가 수수료 정책을 업데이트하려고 하는 경우 */
@Serializable
@SerialName("PLATFORM_ARCHIVED_ADDITIONAL_FEE_POLICY")
@ConsistentCopyVisibility
public data class PlatformArchivedAdditionalFeePolicyError internal constructor(
  override val message: String? = null,
): ScheduleAdditionalFeePolicyError,
  UpdatePlatformAdditionalFeePolicyError

package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 보관된 할인 분담 정책을 업데이트하려고 하는 경우 */
@Serializable
@SerialName("PLATFORM_ARCHIVED_DISCOUNT_SHARE_POLICY")
internal data class PlatformArchivedDiscountSharePolicyError(
  override val message: String? = null,
) : ScheduleDiscountSharePolicyError.Recognized, UpdatePlatformDiscountSharePolicyError.Recognized

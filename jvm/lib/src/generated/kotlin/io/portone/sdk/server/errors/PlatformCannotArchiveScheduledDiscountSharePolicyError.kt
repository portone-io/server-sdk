package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ArchivePlatformDiscountSharePolicyError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 예약된 업데이트가 있는 할인 분담 정책을 보관하려고 하는 경우 */
@Serializable
@SerialName("PLATFORM_CANNOT_ARCHIVE_SCHEDULED_DISCOUNT_SHARE_POLICY")
public data class PlatformCannotArchiveScheduledDiscountSharePolicyError(
  override val message: String? = null,
): ArchivePlatformDiscountSharePolicyError

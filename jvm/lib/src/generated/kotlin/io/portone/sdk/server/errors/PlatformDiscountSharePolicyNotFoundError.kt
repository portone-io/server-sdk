package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ArchivePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.CancelPlatformDiscountSharePolicyScheduleError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyScheduleError
import io.portone.sdk.server.errors.RecoverPlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.RescheduleDiscountSharePolicyError
import io.portone.sdk.server.errors.ScheduleDiscountSharePolicyError
import io.portone.sdk.server.errors.UpdatePlatformDiscountSharePolicyError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND")
public data class PlatformDiscountSharePolicyNotFoundError(
  override val message: String? = null,
): ArchivePlatformDiscountSharePolicyError,
  CancelPlatformDiscountSharePolicyScheduleError,
  GetPlatformDiscountSharePolicyError,
  GetPlatformDiscountSharePolicyScheduleError,
  RecoverPlatformDiscountSharePolicyError,
  RescheduleDiscountSharePolicyError,
  ScheduleDiscountSharePolicyError,
  UpdatePlatformDiscountSharePolicyError

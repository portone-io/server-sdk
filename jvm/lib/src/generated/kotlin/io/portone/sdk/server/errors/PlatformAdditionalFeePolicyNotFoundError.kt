package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ArchivePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.CancelPlatformAdditionalFeePolicyScheduleError
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePolicyScheduleError
import io.portone.sdk.server.errors.RecoverPlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.RescheduleAdditionalFeePolicyError
import io.portone.sdk.server.errors.ScheduleAdditionalFeePolicyError
import io.portone.sdk.server.errors.UpdatePlatformAdditionalFeePolicyError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformAdditionalFeePolicyNotFoundError internal constructor(
  override val message: String? = null,
): ArchivePlatformAdditionalFeePolicyError,
  CancelPlatformAdditionalFeePolicyScheduleError,
  GetPlatformAdditionalFeePolicyError,
  GetPlatformAdditionalFeePolicyScheduleError,
  RecoverPlatformAdditionalFeePolicyError,
  RescheduleAdditionalFeePolicyError,
  ScheduleAdditionalFeePolicyError,
  UpdatePlatformAdditionalFeePolicyError

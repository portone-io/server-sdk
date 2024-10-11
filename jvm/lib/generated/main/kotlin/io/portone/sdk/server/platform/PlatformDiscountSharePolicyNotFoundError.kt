package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND")
public data class PlatformDiscountSharePolicyNotFoundError(
  override val message: String? = null,
): ArchivePlatformDiscountSharePolicyError,
  ): CancelPlatformDiscountSharePolicyScheduleError,
    ): GetPlatformDiscountSharePolicyError,
      ): GetPlatformDiscountSharePolicyScheduleError,
        ): RecoverPlatformDiscountSharePolicyError,
          ): RescheduleDiscountSharePolicyError,
            ): ScheduleDiscountSharePolicyError,
              ): UpdatePlatformDiscountSharePolicyError,

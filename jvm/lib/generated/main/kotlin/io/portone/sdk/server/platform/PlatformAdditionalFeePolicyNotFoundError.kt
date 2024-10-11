package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND")
public data class PlatformAdditionalFeePolicyNotFoundError(
  override val message: String? = null,
): ArchivePlatformAdditionalFeePolicyError,
  ): CancelPlatformAdditionalFeePolicyScheduleError,
    ): GetPlatformAdditionalFeePolicyError,
      ): GetPlatformAdditionalFeePolicyScheduleError,
        ): RecoverPlatformAdditionalFeePolicyError,
          ): RescheduleAdditionalFeePolicyError,
            ): ScheduleAdditionalFeePolicyError,
              ): UpdatePlatformAdditionalFeePolicyError,

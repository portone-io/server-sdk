package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_NOT_FOUND")
public data class PlatformPartnerNotFoundError(
  override val message: String? = null,
): ArchivePlatformPartnerError,
  ): CancelPlatformPartnerScheduleError,
    ): CreatePlatformManualTransferError,
      ): CreatePlatformOrderTransferError,
        ): GetPlatformPartnerError,
          ): GetPlatformPartnerScheduleError,
            ): RecoverPlatformPartnerError,
              ): ReschedulePartnerError,
                ): SchedulePartnerError,
                  ): UpdatePlatformPartnerError,

package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CONTRACT_NOT_FOUND")
public data class PlatformContractNotFoundError(
  override val message: String? = null,
): ArchivePlatformContractError,
  ): CancelPlatformContractScheduleError,
    ): CreatePlatformOrderTransferError,
      ): CreatePlatformPartnerError,
        ): GetPlatformContractError,
          ): GetPlatformContractScheduleError,
            ): RecoverPlatformContractError,
              ): RescheduleContractError,
                ): ReschedulePartnerError,
                  ): ScheduleContractError,
                    ): SchedulePartnerError,
                      ): SchedulePlatformPartnersError,
                        ): UpdatePlatformContractError,
                          ): UpdatePlatformPartnerError,

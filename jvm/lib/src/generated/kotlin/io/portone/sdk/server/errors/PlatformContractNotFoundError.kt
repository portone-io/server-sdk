package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CONTRACT_NOT_FOUND")
internal data class PlatformContractNotFoundError(
  override val message: String? = null,
) : ArchivePlatformContractError.Recognized, CancelPlatformContractScheduleError.Recognized, CreatePlatformOrderTransferError.Recognized, CreatePlatformPartnerError.Recognized, GetPlatformContractError.Recognized, GetPlatformContractScheduleError.Recognized, RecoverPlatformContractError.Recognized, RescheduleContractError.Recognized, ReschedulePartnerError.Recognized, ScheduleContractError.Recognized, SchedulePartnerError.Recognized, SchedulePlatformPartnersError.Recognized, UpdatePlatformContractError.Recognized, UpdatePlatformPartnerError.Recognized

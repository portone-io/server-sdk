package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CONTRACT_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformContractNotFoundError internal constructor(
  val message: String? = null,
) : ArchivePlatformContractError, CancelPlatformContractScheduleError, CreatePlatformOrderTransferError, CreatePlatformPartnerError, GetPlatformContractError, GetPlatformContractScheduleError, RecoverPlatformContractError, RescheduleContractError, ReschedulePartnerError, ScheduleContractError, SchedulePartnerError, SchedulePlatformPartnersError, UpdatePlatformContractError, UpdatePlatformPartnerError

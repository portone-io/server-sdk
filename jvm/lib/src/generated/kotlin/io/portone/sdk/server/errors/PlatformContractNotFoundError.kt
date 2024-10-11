package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ArchivePlatformContractError
import io.portone.sdk.server.errors.CancelPlatformContractScheduleError
import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import io.portone.sdk.server.errors.CreatePlatformPartnerError
import io.portone.sdk.server.errors.GetPlatformContractError
import io.portone.sdk.server.errors.GetPlatformContractScheduleError
import io.portone.sdk.server.errors.RecoverPlatformContractError
import io.portone.sdk.server.errors.RescheduleContractError
import io.portone.sdk.server.errors.ReschedulePartnerError
import io.portone.sdk.server.errors.ScheduleContractError
import io.portone.sdk.server.errors.SchedulePartnerError
import io.portone.sdk.server.errors.SchedulePlatformPartnersError
import io.portone.sdk.server.errors.UpdatePlatformContractError
import io.portone.sdk.server.errors.UpdatePlatformPartnerError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CONTRACT_NOT_FOUND")
public data class PlatformContractNotFoundError(
  val message: String? = null,
): ArchivePlatformContractError,
  CancelPlatformContractScheduleError,
  CreatePlatformOrderTransferError,
  CreatePlatformPartnerError,
  GetPlatformContractError,
  GetPlatformContractScheduleError,
  RecoverPlatformContractError,
  RescheduleContractError,
  ReschedulePartnerError,
  ScheduleContractError,
  SchedulePartnerError,
  SchedulePlatformPartnersError,
  UpdatePlatformContractError,
  UpdatePlatformPartnerError

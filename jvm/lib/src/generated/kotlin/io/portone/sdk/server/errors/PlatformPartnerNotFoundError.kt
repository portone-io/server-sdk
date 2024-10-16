package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ArchivePlatformPartnerError
import io.portone.sdk.server.errors.CancelPlatformPartnerScheduleError
import io.portone.sdk.server.errors.CreatePlatformManualTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import io.portone.sdk.server.errors.GetPlatformPartnerError
import io.portone.sdk.server.errors.GetPlatformPartnerScheduleError
import io.portone.sdk.server.errors.RecoverPlatformPartnerError
import io.portone.sdk.server.errors.ReschedulePartnerError
import io.portone.sdk.server.errors.SchedulePartnerError
import io.portone.sdk.server.errors.UpdatePlatformPartnerError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformPartnerNotFoundError internal constructor(
  override val message: String? = null,
): ArchivePlatformPartnerError,
  CancelPlatformPartnerScheduleError,
  CreatePlatformManualTransferError,
  CreatePlatformOrderTransferError,
  GetPlatformPartnerError,
  GetPlatformPartnerScheduleError,
  RecoverPlatformPartnerError,
  ReschedulePartnerError,
  SchedulePartnerError,
  UpdatePlatformPartnerError

package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_NOT_FOUND")
internal data class PlatformPartnerNotFoundError(
  override val message: String? = null,
) : ArchivePlatformPartnerError.Recognized, CancelPlatformPartnerScheduleError.Recognized, CreatePlatformManualTransferError.Recognized, CreatePlatformOrderTransferError.Recognized, GetPlatformPartnerError.Recognized, GetPlatformPartnerScheduleError.Recognized, RecoverPlatformPartnerError.Recognized, ReschedulePartnerError.Recognized, SchedulePartnerError.Recognized, UpdatePlatformPartnerError.Recognized

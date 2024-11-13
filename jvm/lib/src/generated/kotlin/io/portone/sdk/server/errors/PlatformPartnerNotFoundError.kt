package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformPartnerNotFoundError internal constructor(
  val message: String? = null,
) : ArchivePlatformPartnerError, CancelPlatformPartnerScheduleError, CreatePlatformManualTransferError, CreatePlatformOrderTransferError, GetPlatformPartnerError, GetPlatformPartnerScheduleError, RecoverPlatformPartnerError, ReschedulePartnerError, SchedulePartnerError, UpdatePlatformPartnerError

package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.SchedulePartnerError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_SCHEDULE_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PlatformPartnerScheduleAlreadyExistsError internal constructor(
  override val message: String? = null,
): SchedulePartnerError

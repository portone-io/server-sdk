package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.SchedulePartnerError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_SCHEDULE_ALREADY_EXISTS")
public data class PlatformPartnerScheduleAlreadyExistsError(
  val message: String? = null,
): SchedulePartnerError

package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_SCHEDULE_ALREADY_EXISTS")
internal data class PlatformPartnerScheduleAlreadyExistsError(
  override val message: String? = null,
) : SchedulePartnerError.Recognized

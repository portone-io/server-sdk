package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ADDITIONAL_FEE_POLICY_SCHEDULE_ALREADY_EXISTS")
internal data class PlatformAdditionalFeePolicyScheduleAlreadyExistsError(
  override val message: String? = null,
) : ScheduleAdditionalFeePolicyError.Recognized

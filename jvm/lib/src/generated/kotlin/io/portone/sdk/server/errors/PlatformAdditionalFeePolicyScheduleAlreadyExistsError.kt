package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ScheduleAdditionalFeePolicyError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ADDITIONAL_FEE_POLICY_SCHEDULE_ALREADY_EXISTS")
public data class PlatformAdditionalFeePolicyScheduleAlreadyExistsError(
  val message: String? = null,
): ScheduleAdditionalFeePolicyError

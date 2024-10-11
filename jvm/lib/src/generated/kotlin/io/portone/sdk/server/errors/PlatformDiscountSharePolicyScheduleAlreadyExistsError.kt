package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ScheduleDiscountSharePolicyError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS")
public data class PlatformDiscountSharePolicyScheduleAlreadyExistsError(
  val message: String? = null,
): ScheduleDiscountSharePolicyError

package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS")
internal data class PlatformDiscountSharePolicyScheduleAlreadyExistsError(
  override val message: String? = null,
) : ScheduleDiscountSharePolicyError.Recognized

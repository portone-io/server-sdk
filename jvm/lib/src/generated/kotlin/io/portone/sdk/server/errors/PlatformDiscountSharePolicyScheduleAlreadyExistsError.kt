package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ScheduleDiscountSharePolicyError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PlatformDiscountSharePolicyScheduleAlreadyExistsError internal constructor(
  override val message: String? = null,
): ScheduleDiscountSharePolicyError

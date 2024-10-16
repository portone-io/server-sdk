package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformDiscountSharePolicyError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICY_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PlatformDiscountSharePolicyAlreadyExistsError internal constructor(
  override val message: String? = null,
): CreatePlatformDiscountSharePolicyError

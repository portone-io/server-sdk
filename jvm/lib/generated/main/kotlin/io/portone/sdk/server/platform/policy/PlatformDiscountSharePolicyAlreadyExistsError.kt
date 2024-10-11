package io.portone.sdk.server.platform.policy

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICY_ALREADY_EXISTS")
public data class PlatformDiscountSharePolicyAlreadyExistsError(
  override val message: String? = null,
): CreatePlatformDiscountSharePolicyError,

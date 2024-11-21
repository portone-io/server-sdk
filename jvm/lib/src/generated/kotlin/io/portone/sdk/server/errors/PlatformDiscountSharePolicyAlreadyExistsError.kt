package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICY_ALREADY_EXISTS")
internal data class PlatformDiscountSharePolicyAlreadyExistsError(
  override val message: String? = null,
) : CreatePlatformDiscountSharePolicyError.Recognized

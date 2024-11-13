package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICY_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PlatformDiscountSharePolicyAlreadyExistsError internal constructor(
  val message: String? = null,
) : CreatePlatformDiscountSharePolicyError

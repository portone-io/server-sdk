package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformAdditionalFeePolicyError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ADDITIONAL_FEE_POLICY_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PlatformAdditionalFeePolicyAlreadyExistsError internal constructor(
  override val message: String? = null,
): CreatePlatformAdditionalFeePolicyError

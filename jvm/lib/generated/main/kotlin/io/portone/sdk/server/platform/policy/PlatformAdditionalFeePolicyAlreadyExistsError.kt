package io.portone.sdk.server.platform.policy

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ADDITIONAL_FEE_POLICY_ALREADY_EXISTS")
public data class PlatformAdditionalFeePolicyAlreadyExistsError(
  override val message: String? = null,
): CreatePlatformAdditionalFeePolicyError,

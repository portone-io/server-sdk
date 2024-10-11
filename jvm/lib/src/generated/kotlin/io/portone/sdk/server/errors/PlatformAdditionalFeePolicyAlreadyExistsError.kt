package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformAdditionalFeePolicyError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ADDITIONAL_FEE_POLICY_ALREADY_EXISTS")
public data class PlatformAdditionalFeePolicyAlreadyExistsError(
  val message: String? = null,
): CreatePlatformAdditionalFeePolicyError

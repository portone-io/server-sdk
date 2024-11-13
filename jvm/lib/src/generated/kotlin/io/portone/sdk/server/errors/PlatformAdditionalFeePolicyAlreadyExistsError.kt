package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ADDITIONAL_FEE_POLICY_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PlatformAdditionalFeePolicyAlreadyExistsError internal constructor(
  val message: String? = null,
) : CreatePlatformAdditionalFeePolicyError

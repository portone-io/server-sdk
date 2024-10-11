package io.portone.sdk.server.platform.policy

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CONTRACT_ALREADY_EXISTS")
public data class PlatformContractAlreadyExistsError(
  override val message: String? = null,
): CreatePlatformContractError,

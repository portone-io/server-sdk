package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CONTRACT_ALREADY_EXISTS")
internal data class PlatformContractAlreadyExistsError(
  override val message: String? = null,
) : CreatePlatformContractError.Recognized

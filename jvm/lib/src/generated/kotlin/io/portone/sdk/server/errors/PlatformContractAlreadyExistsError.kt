package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CONTRACT_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PlatformContractAlreadyExistsError internal constructor(
  val message: String? = null,
) : CreatePlatformContractError

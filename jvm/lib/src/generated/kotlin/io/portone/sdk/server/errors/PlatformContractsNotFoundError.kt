package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformPartnersError
import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CONTRACTS_NOT_FOUND")
public data class PlatformContractsNotFoundError(
  val ids: Array<String>,
  val graphqlIds: Array<String>,
  val message: String? = null,
): CreatePlatformPartnersError

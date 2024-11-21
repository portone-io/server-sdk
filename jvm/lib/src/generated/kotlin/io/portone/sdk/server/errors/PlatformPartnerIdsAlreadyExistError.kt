package io.portone.sdk.server.errors

import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_IDS_ALREADY_EXISTS")
internal data class PlatformPartnerIdsAlreadyExistError(
  val ids: List<String>,
  val graphqlIds: List<String>,
  override val message: String? = null,
) : CreatePlatformPartnersError.Recognized

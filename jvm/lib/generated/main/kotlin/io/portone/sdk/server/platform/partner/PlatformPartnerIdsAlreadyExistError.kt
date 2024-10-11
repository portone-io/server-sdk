package io.portone.sdk.server.platform.partner

import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_IDS_ALREADY_EXISTS")
public data class PlatformPartnerIdsAlreadyExistError(
  val ids: Array<String>,
  val graphqlIds: Array<String>,
  override val message: String? = null,
): CreatePlatformPartnersError,

package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformPartnersError
import kotlin.Array
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_IDS_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PlatformPartnerIdsAlreadyExistError internal constructor(
  val ids: List<String>,
  val graphqlIds: List<String>,
  override val message: String? = null,
): CreatePlatformPartnersError

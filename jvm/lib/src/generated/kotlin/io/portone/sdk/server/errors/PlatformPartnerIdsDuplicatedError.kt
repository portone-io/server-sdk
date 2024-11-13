package io.portone.sdk.server.errors

import kotlin.Array
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_IDS_DUPLICATED")
@ConsistentCopyVisibility
public data class PlatformPartnerIdsDuplicatedError internal constructor(
  val ids: List<String>,
  val graphqlIds: List<String>,
  val message: String? = null,
) : CreatePlatformPartnersError

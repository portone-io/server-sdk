package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_ID_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PlatformPartnerIdAlreadyExistsError internal constructor(
  val message: String? = null,
) : CreatePlatformPartnerError

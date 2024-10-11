package io.portone.sdk.server.platform.partner

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_ID_ALREADY_EXISTS")
public data class PlatformPartnerIdAlreadyExistsError(
  override val message: String? = null,
): CreatePlatformPartnerError,

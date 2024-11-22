package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_ID_ALREADY_EXISTS")
internal data class PlatformPartnerIdAlreadyExistsError(
  override val message: String? = null,
) : CreatePlatformPartnerError.Recognized



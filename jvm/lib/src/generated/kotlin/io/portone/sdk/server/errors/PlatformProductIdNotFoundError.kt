package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PRODUCT_ID_NOT_FOUND")
internal data class PlatformProductIdNotFoundError(
  val id: String,
  override val message: String? = null,
) : CreatePlatformOrderCancelTransferError.Recognized

package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_NOT_FOUND")
internal data class PlatformTransferNotFoundError(
  override val message: String? = null,
) : CreatePlatformOrderCancelTransferError.Recognized, DeletePlatformTransferError.Recognized, GetPlatformTransferError.Recognized

package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ORDER_TRANSFER_ALREADY_CANCELLED")
internal data class PlatformOrderTransferAlreadyCancelledError(
  override val message: String? = null,
) : CreatePlatformOrderCancelTransferError.Recognized

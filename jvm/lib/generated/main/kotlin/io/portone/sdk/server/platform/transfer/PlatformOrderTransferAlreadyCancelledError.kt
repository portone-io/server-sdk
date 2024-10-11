package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ORDER_TRANSFER_ALREADY_CANCELLED")
public data class PlatformOrderTransferAlreadyCancelledError(
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError,

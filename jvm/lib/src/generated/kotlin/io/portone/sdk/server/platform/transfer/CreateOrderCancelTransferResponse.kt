package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.PlatformOrderCancelTransfer
import kotlinx.serialization.Serializable

@Serializable
public data class CreateOrderCancelTransferResponse(
  val transfer: PlatformOrderCancelTransfer,
)

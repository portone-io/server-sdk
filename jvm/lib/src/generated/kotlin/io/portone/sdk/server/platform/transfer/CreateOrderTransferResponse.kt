package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.PlatformOrderTransfer
import kotlinx.serialization.Serializable

@Serializable
public data class CreateOrderTransferResponse(
  val transfer: PlatformOrderTransfer,
)

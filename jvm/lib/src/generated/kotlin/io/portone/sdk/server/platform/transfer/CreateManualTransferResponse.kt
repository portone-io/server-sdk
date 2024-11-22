package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.PlatformManualTransfer
import kotlinx.serialization.Serializable

@Serializable
public data class CreateManualTransferResponse(
  val transfer: PlatformManualTransfer,
)



package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CANCEL_ORDER_TRANSFERS_EXISTS")
internal data class PlatformCancelOrderTransfersExistsError(
  override val message: String? = null,
) : DeletePlatformTransferError.Recognized



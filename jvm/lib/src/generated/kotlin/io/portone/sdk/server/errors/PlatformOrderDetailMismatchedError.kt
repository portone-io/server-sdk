package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ORDER_DETAIL_MISMATCHED")
internal data class PlatformOrderDetailMismatchedError(
  override val message: String? = null,
) : CreatePlatformOrderCancelTransferError.Recognized



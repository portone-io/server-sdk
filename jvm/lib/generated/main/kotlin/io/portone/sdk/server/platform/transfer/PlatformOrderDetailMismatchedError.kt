package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ORDER_DETAIL_MISMATCHED")
public data class PlatformOrderDetailMismatchedError(
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError,

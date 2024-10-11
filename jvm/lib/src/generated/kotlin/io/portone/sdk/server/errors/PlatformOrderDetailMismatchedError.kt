package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ORDER_DETAIL_MISMATCHED")
public data class PlatformOrderDetailMismatchedError(
  val message: String? = null,
): CreatePlatformOrderCancelTransferError

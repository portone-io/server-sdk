package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED")
public data class PlatformCancellableProductQuantityExceededError(
  val productId: String,
  val cancellableQuantity: Long,
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError,

package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED")
@ConsistentCopyVisibility
public data class PlatformCancellableProductQuantityExceededError internal constructor(
  val productId: String,
  val cancellableQuantity: Long,
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError

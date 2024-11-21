package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCancellableProductQuantityExceededError
import java.lang.Exception
import kotlin.String


public class PlatformCancellableProductQuantityExceededException internal constructor(
  cause: PlatformCancellableProductQuantityExceededError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException {
  public val productId: String = cause.productId
  public val cancellableQuantity: Long = cause.cancellableQuantity
}

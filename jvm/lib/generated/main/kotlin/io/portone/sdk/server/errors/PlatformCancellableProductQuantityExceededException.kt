package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformCancellableProductQuantityExceededError
import java.lang.Exception
import kotlin.String


public class PlatformCancellableProductQuantityExceededException(
  cause: PlatformCancellableProductQuantityExceededError
) : Exception(cause.message) {
  public val productId: String = cause.productId,
  public val cancellableQuantity: Long = cause.cancellableQuantity,
}

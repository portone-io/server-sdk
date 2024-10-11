package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCancellableAmountExceededError
import io.portone.sdk.server.platform.transfer.PlatformCancellableAmountType
import java.lang.Exception


/** 취소 가능한 금액이 초과한 경우 */
public class PlatformCancellableAmountExceededException(
  cause: PlatformCancellableAmountExceededError
) : Exception(cause.message) {
  public val cancellableAmount: Long = cause.cancellableAmount
  public val requestAmount: Long = cause.requestAmount
  public val amountType: PlatformCancellableAmountType = cause.amountType
}

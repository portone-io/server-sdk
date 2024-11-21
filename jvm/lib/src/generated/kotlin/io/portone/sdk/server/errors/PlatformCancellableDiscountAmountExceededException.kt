package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCancellableDiscountAmountExceededError
import java.lang.Exception
import kotlin.String


public class PlatformCancellableDiscountAmountExceededException internal constructor(
  cause: PlatformCancellableDiscountAmountExceededError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException {
  public val discountSharePolicyId: String = cause.discountSharePolicyId
  public val discountSharePolicyGraphqlId: String = cause.discountSharePolicyGraphqlId
  public val cancellableAmount: Long = cause.cancellableAmount
  public val requestAmount: Long = cause.requestAmount
  public val productId: String? = cause.productId
}

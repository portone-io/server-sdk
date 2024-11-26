package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformTransferDiscountSharePolicyNotFoundError
import java.lang.Exception
import kotlin.String


public class PlatformTransferDiscountSharePolicyNotFoundException internal constructor(
  cause: PlatformTransferDiscountSharePolicyNotFoundError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException {
  public val discountSharePolicyId: String = cause.discountSharePolicyId
  public val discountSharePolicyGraphqlId: String = cause.discountSharePolicyGraphqlId
  public val productId: String? = cause.productId
}

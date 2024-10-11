package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformTransferDiscountSharePolicyNotFoundError
import java.lang.Exception
import kotlin.String


public class PlatformTransferDiscountSharePolicyNotFoundException(
  cause: PlatformTransferDiscountSharePolicyNotFoundError
) : Exception(cause.message) {
  public val discountSharePolicyId: String = cause.discountSharePolicyId
  public val discountSharePolicyGraphqlId: String = cause.discountSharePolicyGraphqlId
  public val productId: String? = cause.productId
}

package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CANCELLABLE_DISCOUNT_TAX_FREE_AMOUNT_EXCEEDED")
internal data class PlatformCancellableDiscountTaxFreeAmountExceededError(
  val discountSharePolicyId: String,
  val discountSharePolicyGraphqlId: String,
  val cancellableAmount: Long,
  val requestAmount: Long,
  val productId: String? = null,
  override val message: String? = null,
) : CreatePlatformOrderCancelTransferError.Recognized

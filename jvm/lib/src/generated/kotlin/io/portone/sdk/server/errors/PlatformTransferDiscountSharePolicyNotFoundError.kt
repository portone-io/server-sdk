package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_DISCOUNT_SHARE_POLICY_NOT_FOUND")
internal data class PlatformTransferDiscountSharePolicyNotFoundError(
  val discountSharePolicyId: String,
  val discountSharePolicyGraphqlId: String,
  val productId: String? = null,
  override val message: String? = null,
) : CreatePlatformOrderCancelTransferError.Recognized



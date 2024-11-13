package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_DISCOUNT_SHARE_POLICY_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformTransferDiscountSharePolicyNotFoundError internal constructor(
  val discountSharePolicyId: String,
  val discountSharePolicyGraphqlId: String,
  val productId: String? = null,
  val message: String? = null,
) : CreatePlatformOrderCancelTransferError

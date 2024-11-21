package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICY_ID_DUPLICATED")
internal data class PlatformDiscountSharePolicyIdDuplicatedError(
  val id: String,
  val graphqlId: String,
  override val message: String? = null,
) : CreatePlatformOrderCancelTransferError.Recognized

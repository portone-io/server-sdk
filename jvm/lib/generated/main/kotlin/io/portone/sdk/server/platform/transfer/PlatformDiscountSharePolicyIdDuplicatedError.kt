package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICY_ID_DUPLICATED")
public data class PlatformDiscountSharePolicyIdDuplicatedError(
  val id: String,
  val graphqlId: String,
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError,

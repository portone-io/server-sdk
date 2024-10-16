package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICY_ID_DUPLICATED")
@ConsistentCopyVisibility
public data class PlatformDiscountSharePolicyIdDuplicatedError internal constructor(
  val id: String,
  val graphqlId: String,
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError

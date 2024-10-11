package io.portone.sdk.server.platform.transfer

import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICIES_NOT_FOUND")
public data class PlatformDiscountSharePoliciesNotFoundError(
  val ids: Array<String>,
  val graphqlIds: Array<String>,
  override val message: String? = null,
): CreatePlatformOrderTransferError,

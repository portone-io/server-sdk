package io.portone.sdk.server.errors

import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_DISCOUNT_SHARE_POLICIES_NOT_FOUND")
internal data class PlatformDiscountSharePoliciesNotFoundError(
  val ids: List<String>,
  val graphqlIds: List<String>,
  override val message: String? = null,
) : CreatePlatformOrderTransferError.Recognized

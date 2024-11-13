package io.portone.sdk.server.errors

import kotlin.Array
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ADDITIONAL_FEE_POLICIES_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformAdditionalFeePoliciesNotFoundError internal constructor(
  val ids: List<String>,
  val graphqlIds: List<String>,
  val message: String? = null,
) : CreatePlatformOrderTransferError

package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ORDER_DETAIL_MISMATCHED")
@ConsistentCopyVisibility
public data class PlatformOrderDetailMismatchedError internal constructor(
  val message: String? = null,
) : CreatePlatformOrderCancelTransferError

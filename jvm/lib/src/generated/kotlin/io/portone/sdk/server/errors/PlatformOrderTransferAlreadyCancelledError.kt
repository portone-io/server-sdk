package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ORDER_TRANSFER_ALREADY_CANCELLED")
@ConsistentCopyVisibility
public data class PlatformOrderTransferAlreadyCancelledError internal constructor(
  val message: String? = null,
) : CreatePlatformOrderCancelTransferError

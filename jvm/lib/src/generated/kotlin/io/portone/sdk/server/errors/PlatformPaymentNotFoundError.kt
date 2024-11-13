package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PAYMENT_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformPaymentNotFoundError internal constructor(
  val message: String? = null,
) : CreatePlatformOrderCancelTransferError, CreatePlatformOrderTransferError

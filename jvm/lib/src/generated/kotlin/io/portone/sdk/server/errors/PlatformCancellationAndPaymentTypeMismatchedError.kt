package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED")
@ConsistentCopyVisibility
public data class PlatformCancellationAndPaymentTypeMismatchedError internal constructor(
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError

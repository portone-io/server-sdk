package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED")
public data class PlatformCancellationAndPaymentTypeMismatchedError(
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError,

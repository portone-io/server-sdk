package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PAYMENT_NOT_FOUND")
public data class PlatformPaymentNotFoundError(
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError,
  ): CreatePlatformOrderTransferError,

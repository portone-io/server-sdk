package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PAYMENT_NOT_FOUND")
public data class PlatformPaymentNotFoundError(
  val message: String? = null,
): CreatePlatformOrderCancelTransferError,
  CreatePlatformOrderTransferError

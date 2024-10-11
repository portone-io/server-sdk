package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PRODUCT_ID_DUPLICATED")
public data class PlatformProductIdDuplicatedError(
  val id: String,
  val message: String? = null,
): CreatePlatformOrderCancelTransferError,
  CreatePlatformOrderTransferError

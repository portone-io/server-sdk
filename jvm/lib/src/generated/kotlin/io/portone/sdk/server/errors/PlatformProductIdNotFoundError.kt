package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PRODUCT_ID_NOT_FOUND")
public data class PlatformProductIdNotFoundError(
  val id: String,
  val message: String? = null,
): CreatePlatformOrderCancelTransferError

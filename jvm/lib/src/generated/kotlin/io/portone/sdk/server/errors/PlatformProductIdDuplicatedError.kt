package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PRODUCT_ID_DUPLICATED")
@ConsistentCopyVisibility
public data class PlatformProductIdDuplicatedError internal constructor(
  val id: String,
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError,
  CreatePlatformOrderTransferError

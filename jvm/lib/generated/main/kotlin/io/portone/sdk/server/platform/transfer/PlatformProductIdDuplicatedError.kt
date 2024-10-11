package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PRODUCT_ID_DUPLICATED")
public data class PlatformProductIdDuplicatedError(
  val id: String,
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError,
  ): CreatePlatformOrderTransferError,

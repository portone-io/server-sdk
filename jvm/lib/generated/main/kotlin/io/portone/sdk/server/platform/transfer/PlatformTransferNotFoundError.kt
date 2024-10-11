package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_NOT_FOUND")
public data class PlatformTransferNotFoundError(
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError,
  ): DeletePlatformTransferError,
    ): GetPlatformTransferError,

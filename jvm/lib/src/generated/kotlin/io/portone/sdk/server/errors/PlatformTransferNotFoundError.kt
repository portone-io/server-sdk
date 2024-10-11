package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.errors.DeletePlatformTransferError
import io.portone.sdk.server.errors.GetPlatformTransferError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_NOT_FOUND")
public data class PlatformTransferNotFoundError(
  val message: String? = null,
): CreatePlatformOrderCancelTransferError,
  DeletePlatformTransferError,
  GetPlatformTransferError

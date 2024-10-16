package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.errors.DeletePlatformTransferError
import io.portone.sdk.server.errors.GetPlatformTransferError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformTransferNotFoundError internal constructor(
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError,
  DeletePlatformTransferError,
  GetPlatformTransferError

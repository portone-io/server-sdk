package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformTransferNotFoundError internal constructor(
  val message: String? = null,
) : CreatePlatformOrderCancelTransferError, DeletePlatformTransferError, GetPlatformTransferError

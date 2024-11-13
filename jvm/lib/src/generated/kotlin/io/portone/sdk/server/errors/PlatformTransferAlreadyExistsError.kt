package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PlatformTransferAlreadyExistsError internal constructor(
  val transferId: String,
  val transferGraphqlId: String,
  val message: String? = null,
) : CreatePlatformOrderCancelTransferError, CreatePlatformOrderTransferError

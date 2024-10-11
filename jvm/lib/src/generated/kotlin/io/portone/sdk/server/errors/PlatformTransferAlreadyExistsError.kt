package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_ALREADY_EXISTS")
public data class PlatformTransferAlreadyExistsError(
  val transferId: String,
  val transferGraphqlId: String,
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError,
  CreatePlatformOrderTransferError

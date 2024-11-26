package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_ALREADY_EXISTS")
internal data class PlatformTransferAlreadyExistsError(
  val transferId: String,
  val transferGraphqlId: String,
  override val message: String? = null,
) : CreatePlatformOrderCancelTransferError.Recognized, CreatePlatformOrderTransferError.Recognized



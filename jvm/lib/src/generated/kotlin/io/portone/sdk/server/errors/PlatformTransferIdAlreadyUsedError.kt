package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_ID_ALREADY_USED")
internal data class PlatformTransferIdAlreadyUsedError(
  override val message: String? = null,
) : CreatePlatformManualTransferError.Recognized, CreatePlatformOrderCancelTransferError.Recognized, CreatePlatformOrderTransferError.Recognized



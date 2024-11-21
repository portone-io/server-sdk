package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CANCELLATION_NOT_FOUND")
internal data class PlatformCancellationNotFoundError(
  override val message: String? = null,
) : CreatePlatformOrderCancelTransferError.Recognized

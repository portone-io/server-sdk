package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CANCELLATION_NOT_FOUND")
public data class PlatformCancellationNotFoundError(
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError,

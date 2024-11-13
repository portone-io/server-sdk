package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CANCELLATION_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformCancellationNotFoundError internal constructor(
  val message: String? = null,
) : CreatePlatformOrderCancelTransferError

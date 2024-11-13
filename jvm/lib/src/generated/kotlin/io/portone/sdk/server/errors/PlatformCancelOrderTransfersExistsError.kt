package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CANCEL_ORDER_TRANSFERS_EXISTS")
@ConsistentCopyVisibility
public data class PlatformCancelOrderTransfersExistsError internal constructor(
  val message: String? = null,
) : DeletePlatformTransferError

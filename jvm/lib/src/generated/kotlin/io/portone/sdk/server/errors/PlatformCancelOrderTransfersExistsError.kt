package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.DeletePlatformTransferError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CANCEL_ORDER_TRANSFERS_EXISTS")
public data class PlatformCancelOrderTransfersExistsError(
  val message: String? = null,
): DeletePlatformTransferError

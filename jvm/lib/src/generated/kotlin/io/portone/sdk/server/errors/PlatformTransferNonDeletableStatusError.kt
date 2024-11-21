package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_NON_DELETABLE_STATUS")
internal data class PlatformTransferNonDeletableStatusError(
  override val message: String? = null,
) : DeletePlatformTransferError.Recognized

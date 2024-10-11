package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_NON_DELETABLE_STATUS")
public data class PlatformTransferNonDeletableStatusError(
  override val message: String? = null,
): DeletePlatformTransferError,

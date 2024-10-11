package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.DeletePlatformTransferError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_NON_DELETABLE_STATUS")
public data class PlatformTransferNonDeletableStatusError(
  val message: String? = null,
): DeletePlatformTransferError

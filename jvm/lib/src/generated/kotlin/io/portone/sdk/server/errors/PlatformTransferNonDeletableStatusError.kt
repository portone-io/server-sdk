package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_TRANSFER_NON_DELETABLE_STATUS")
@ConsistentCopyVisibility
public data class PlatformTransferNonDeletableStatusError internal constructor(
  val message: String? = null,
) : DeletePlatformTransferError

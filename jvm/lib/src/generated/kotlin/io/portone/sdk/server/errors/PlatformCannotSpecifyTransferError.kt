package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 건 식별에 실패한 경우 */
@Serializable
@SerialName("PLATFORM_CANNOT_SPECIFY_TRANSFER")
@ConsistentCopyVisibility
public data class PlatformCannotSpecifyTransferError internal constructor(
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError

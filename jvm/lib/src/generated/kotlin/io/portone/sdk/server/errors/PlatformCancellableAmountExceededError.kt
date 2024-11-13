package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformCancellableAmountType
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 취소 가능한 금액이 초과한 경우 */
@Serializable
@SerialName("PLATFORM_CANCELLABLE_AMOUNT_EXCEEDED")
@ConsistentCopyVisibility
public data class PlatformCancellableAmountExceededError internal constructor(
  val cancellableAmount: Long,
  val requestAmount: Long,
  val amountType: PlatformCancellableAmountType,
  val message: String? = null,
) : CreatePlatformOrderCancelTransferError

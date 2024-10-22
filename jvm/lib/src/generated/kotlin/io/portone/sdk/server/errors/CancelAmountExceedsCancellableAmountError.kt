package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CancelPaymentError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 취소 금액이 취소 가능 금액을 초과한 경우 */
@Serializable
@SerialName("CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT")
@ConsistentCopyVisibility
public data class CancelAmountExceedsCancellableAmountError internal constructor(
  override val message: String? = null,
): CancelPaymentError

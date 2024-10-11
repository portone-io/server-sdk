package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 취소 금액이 취소 가능 금액을 초과한 경우 */
@Serializable
@SerialName("CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT")
public data class CancelAmountExceedsCancellableAmountError(
  override val message: String? = null,
): CancelPaymentError,

package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CancelPaymentError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 취소 가능 잔액 검증에 실패한 경우 */
@Serializable
@SerialName("CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN")
public data class CancellableAmountConsistencyBrokenError(
  val message: String? = null,
): CancelPaymentError

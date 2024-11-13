package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 취소 가능 잔액 검증에 실패한 경우 */
@Serializable
@SerialName("CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN")
@ConsistentCopyVisibility
public data class CancellableAmountConsistencyBrokenError internal constructor(
  val message: String? = null,
) : CancelPaymentError

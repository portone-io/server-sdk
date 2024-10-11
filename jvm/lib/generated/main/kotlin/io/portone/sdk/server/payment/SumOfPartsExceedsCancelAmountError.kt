package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우 */
@Serializable
@SerialName("SUM_OF_PARTS_EXCEEDS_CANCEL_AMOUNT")
public data class SumOfPartsExceedsCancelAmountError(
  override val message: String? = null,
): CancelPaymentError,

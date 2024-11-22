package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우 */
@Serializable
@SerialName("SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT")
internal data class SumOfPartsExceedsTotalAmountError(
  override val message: String? = null,
) : CreatePaymentScheduleError.Recognized, PayInstantlyError.Recognized, PayWithBillingKeyError.Recognized



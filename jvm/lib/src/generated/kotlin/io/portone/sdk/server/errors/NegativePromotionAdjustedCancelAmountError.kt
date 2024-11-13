package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 프로모션에 의해 조정된 취소 금액이 음수인 경우 */
@Serializable
@SerialName("NEGATIVE_PROMOTION_ADJUSTED_CANCEL_AMOUNT")
@ConsistentCopyVisibility
public data class NegativePromotionAdjustedCancelAmountError internal constructor(
  val message: String? = null,
) : CancelPaymentError

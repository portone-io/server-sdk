package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PayInstantlyError
import io.portone.sdk.server.errors.PayWithBillingKeyError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 프로모션 할인 금액이 결제 시도 금액 이상인 경우 */
@Serializable
@SerialName("DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT")
@ConsistentCopyVisibility
public data class DiscountAmountExceedsTotalAmountError internal constructor(
  override val message: String? = null,
): PayInstantlyError,
  PayWithBillingKeyError

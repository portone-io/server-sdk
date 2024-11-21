package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 프로모션 혜택 유지 옵션을 이전 부분 취소와 다른 것으로 입력한 경우 */
@Serializable
@SerialName("PROMOTION_DISCOUNT_RETAIN_OPTION_SHOULD_NOT_BE_CHANGED")
internal data class PromotionDiscountRetainOptionShouldNotBeChangedError(
  override val message: String? = null,
) : CancelPaymentError.Recognized

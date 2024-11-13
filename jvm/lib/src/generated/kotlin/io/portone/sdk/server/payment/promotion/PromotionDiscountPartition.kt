package io.portone.sdk.server.payment.promotion

import io.portone.sdk.server.payment.promotion.PromotionDiscountScheme
import kotlinx.serialization.Serializable

/** 금액 구간별 프로모션 할인 정책 */
@Serializable
public data class PromotionDiscountPartition(
  val amountFrom: Long,
  val scheme: PromotionDiscountScheme,
)

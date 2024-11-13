package io.portone.sdk.server.payment.promotion

import io.portone.sdk.server.payment.promotion.PromotionDiscountPartition
import kotlinx.serialization.Serializable

/** 프로모션 할인 정책 */
@Serializable
public data class PromotionDiscountPolicy(
  /** 금액 구간별 프로모션 할인 정책 */
  val partitions: List<PromotionDiscountPartition>,
)

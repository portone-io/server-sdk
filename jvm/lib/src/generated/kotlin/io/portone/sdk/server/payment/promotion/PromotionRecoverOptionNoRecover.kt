package io.portone.sdk.server.payment.promotion

import io.portone.sdk.server.payment.promotion.PromotionSpareBudget
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 취소 시 프로모션 예산 미복구 */
@Serializable
@SerialName("NO_RECOVER")
public data class PromotionRecoverOptionNoRecover(
  val spareBudget: PromotionSpareBudget? = null,
) : PromotionRecoverOption

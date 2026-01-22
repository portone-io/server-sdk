package io.portone.sdk.server.payment.additionalfeature

import io.portone.sdk.server.payment.additionalfeature.PgCardPromotion
import kotlinx.serialization.Serializable

/** PG사 카드 프로모션 조회 응답 */
@Serializable
public data class GetPgCardPromotionsResponse(
  /** 카드 프로모션 목록 */
  val promotions: List<PgCardPromotion>? = null,
)



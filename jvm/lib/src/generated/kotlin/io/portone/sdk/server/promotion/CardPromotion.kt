package io.portone.sdk.server.promotion

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.promotion.Promotion
import io.portone.sdk.server.promotion.PromotionCardCompany
import io.portone.sdk.server.promotion.PromotionDiscount
import io.portone.sdk.server.promotion.PromotionStatus
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 카드 프로모션 */
@Serializable
@SerialName("CARD")
public data class CardPromotion(
  /** 프로모션 아이디 */
  override val id: String,
  /** 상점 아이디 */
  override val storeId: String,
  /** 프로모션 이름 */
  override val name: String,
  /** 할인 유형 */
  override val discountType: PromotionDiscount,
  /** 총 예산 */
  override val totalBudget: Long,
  /** 소진 금액 */
  override val spentAmount: Long,
  /** 금액 화폐 */
  override val currency: Currency,
  /** 프로모션 시작 시각 */
  override val startAt: Instant,
  /** 프로모션 종료 시각 */
  override val endAt: Instant,
  /** 프로모션 카드사 */
  override val cardCompany: PromotionCardCompany,
  /** 프로모션 상태 */
  override val status: PromotionStatus,
  /** 프로모션 생성 시각 */
  override val createdAt: Instant,
  /** 최소 결제 금액 */
  override val minPaymentAmount: Long? = null,
  /** 최대 할인 금액 */
  override val maxDiscountAmount: Long? = null,
  /** 프로모션 중단 시각 */
  override val terminatedAt: Instant? = null,
): Promotion

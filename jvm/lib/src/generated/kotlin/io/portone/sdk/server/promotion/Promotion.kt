package io.portone.sdk.server.promotion

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.promotion.PromotionCardCompany
import io.portone.sdk.server.promotion.PromotionDiscount
import io.portone.sdk.server.promotion.PromotionStatus
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 프로모션 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface Promotion {
  /** 프로모션 아이디 */
  public val id: String
  /** 상점 아이디 */
  public val storeId: String
  /** 프로모션 이름 */
  public val name: String
  /** 할인 유형 */
  public val discountType: PromotionDiscount
  /** 총 예산 */
  public val totalBudget: Long
  /** 최소 결제 금액 */
  public val minPaymentAmount: Long?
  /** 최대 할인 금액 */
  public val maxDiscountAmount: Long?
  /** 소진 금액 */
  public val spentAmount: Long
  /** 금액 화폐 */
  public val currency: Currency
  /** 프로모션 시작 시각 */
  public val startAt: Instant
  /** 프로모션 종료 시각 */
  public val endAt: Instant
  /** 프로모션 중단 시각 */
  public val terminatedAt: Instant?
  /** 프로모션 카드사 */
  public val cardCompany: PromotionCardCompany
  /** 프로모션 상태 */
  public val status: PromotionStatus
  /** 프로모션 생성 시각 */
  public val createdAt: Instant
}

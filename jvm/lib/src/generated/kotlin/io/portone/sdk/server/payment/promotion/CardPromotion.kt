package io.portone.sdk.server.payment.promotion

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.payment.promotion.PromotionCardCompany
import io.portone.sdk.server.payment.promotion.PromotionDiscountPolicy
import io.portone.sdk.server.payment.promotion.PromotionRecoverOption
import io.portone.sdk.server.payment.promotion.PromotionStatus
import io.portone.sdk.server.serializers.InstantSerializer
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
  /** 할인 정책 */
  override val discountPolicy: PromotionDiscountPolicy,
  /** 총 예산 */
  override val totalBudget: Long,
  /** 최대 할인 금액 */
  override val maxDiscountAmount: Long? = null,
  /** 소진 금액 */
  override val spentAmount: Long,
  /** 금액 화폐 */
  override val currency: Currency,
  /** 프로모션 시작 시각 */
  override val startAt: @Serializable(InstantSerializer::class) Instant,
  /** 프로모션 종료 시각 */
  override val endAt: @Serializable(InstantSerializer::class) Instant,
  /** 프로모션 중단 시각 */
  override val terminatedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 프로모션 카드사 */
  override val cardCompany: PromotionCardCompany,
  /** 프로모션 상태 */
  override val status: PromotionStatus,
  /** 프로모션 생성 시각 */
  override val createdAt: @Serializable(InstantSerializer::class) Instant,
  /** 결제 취소 시 프로모션 예산 복구 옵션 */
  override val recoverOption: PromotionRecoverOption,
) : Promotion.Recognized

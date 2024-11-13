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
  val id: String,
  /** 상점 아이디 */
  val storeId: String,
  /** 프로모션 이름 */
  val name: String,
  /** 할인 정책 */
  val discountPolicy: PromotionDiscountPolicy,
  /** 총 예산 */
  val totalBudget: Long,
  /** 소진 금액 */
  val spentAmount: Long,
  /** 금액 화폐 */
  val currency: Currency,
  /** 프로모션 시작 시각 */
  val startAt: @Serializable(InstantSerializer::class) Instant,
  /** 프로모션 종료 시각 */
  val endAt: @Serializable(InstantSerializer::class) Instant,
  /** 프로모션 카드사 */
  val cardCompany: PromotionCardCompany,
  /** 프로모션 상태 */
  val status: PromotionStatus,
  /** 프로모션 생성 시각 */
  val createdAt: @Serializable(InstantSerializer::class) Instant,
  /** 결제 취소 시 프로모션 예산 복구 옵션 */
  val recoverOption: PromotionRecoverOption,
  /** 최대 할인 금액 */
  val maxDiscountAmount: Long? = null,
  /** 프로모션 중단 시각 */
  val terminatedAt: @Serializable(InstantSerializer::class) Instant? = null,
) : Promotion

package io.portone.sdk.server.payment.promotion

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.payment.promotion.PromotionCardCompany
import io.portone.sdk.server.payment.promotion.PromotionDiscountPolicy
import io.portone.sdk.server.payment.promotion.PromotionRecoverOption
import io.portone.sdk.server.payment.promotion.PromotionStatus
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 프로모션 */
@Serializable(PromotionSerializer::class)
public sealed interface Promotion {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : Promotion {
    /** 프로모션 아이디 */
    public val id: String
    /** 상점 아이디 */
    public val storeId: String
    /** 프로모션 이름 */
    public val name: String
    /** 할인 정책 */
    public val discountPolicy: PromotionDiscountPolicy
    /** 총 예산 */
    public val totalBudget: Long
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
    /** 결제 취소 시 프로모션 예산 복구 옵션 */
    public val recoverOption: PromotionRecoverOption
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : Promotion
}


private object PromotionSerializer : JsonContentPolymorphicSerializer<Promotion>(Promotion::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "CARD" -> CardPromotion.serializer()
    else -> Promotion.Unrecognized.serializer()
  }
}

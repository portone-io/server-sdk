package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.Serializable

/** 프로모션 적용 가능한 카드사 */
@Serializable
public enum class PromotionCardCompany {
  /** 우리카드 */
  WooriCard,
  /** BC카드 */
  BcCard,
  /** 삼성카드 */
  SamsungCard,
  /** 신한카드 */
  ShinhanCard,
  /** 현대카드 */
  HyundaiCard,
  /** 롯데카드 */
  LotteCard,
  /** NH카드 */
  NhCard,
  /** 하나카드 */
  HanaCard,
  /** 국민카드 */
  KookminCard,
}

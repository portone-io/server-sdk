package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 프로모션 적용 가능한 카드사 */
@Serializable
public sealed class PromotionCardCompany {
  /** 우리카드 */
  @SerialName("WOORI_CARD")
  public data object WooriCard : PromotionCardCompany()
  /** BC카드 */
  @SerialName("BC_CARD")
  public data object BcCard : PromotionCardCompany()
  /** 삼성카드 */
  @SerialName("SAMSUNG_CARD")
  public data object SamsungCard : PromotionCardCompany()
  /** 신한카드 */
  @SerialName("SHINHAN_CARD")
  public data object ShinhanCard : PromotionCardCompany()
  /** 현대카드 */
  @SerialName("HYUNDAI_CARD")
  public data object HyundaiCard : PromotionCardCompany()
  /** 롯데카드 */
  @SerialName("LOTTE_CARD")
  public data object LotteCard : PromotionCardCompany()
  /** NH카드 */
  @SerialName("NH_CARD")
  public data object NhCard : PromotionCardCompany()
  /** 하나카드 */
  @SerialName("HANA_CARD")
  public data object HanaCard : PromotionCardCompany()
  /** 국민카드 */
  @SerialName("KOOKMIN_CARD")
  public data object KookminCard : PromotionCardCompany()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PromotionCardCompany()
}

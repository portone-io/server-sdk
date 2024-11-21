package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 프로모션 적용 가능한 카드사 */
@Serializable
public sealed interface PromotionCardCompany {
  public val value: String
  /** 우리카드 */
  @SerialName("WOORI_CARD")
  public data object WooriCard : PromotionCardCompany {
    override val value: String = "WOORI_CARD"
  }
  /** BC카드 */
  @SerialName("BC_CARD")
  public data object BcCard : PromotionCardCompany {
    override val value: String = "BC_CARD"
  }
  /** 삼성카드 */
  @SerialName("SAMSUNG_CARD")
  public data object SamsungCard : PromotionCardCompany {
    override val value: String = "SAMSUNG_CARD"
  }
  /** 신한카드 */
  @SerialName("SHINHAN_CARD")
  public data object ShinhanCard : PromotionCardCompany {
    override val value: String = "SHINHAN_CARD"
  }
  /** 현대카드 */
  @SerialName("HYUNDAI_CARD")
  public data object HyundaiCard : PromotionCardCompany {
    override val value: String = "HYUNDAI_CARD"
  }
  /** 롯데카드 */
  @SerialName("LOTTE_CARD")
  public data object LotteCard : PromotionCardCompany {
    override val value: String = "LOTTE_CARD"
  }
  /** NH카드 */
  @SerialName("NH_CARD")
  public data object NhCard : PromotionCardCompany {
    override val value: String = "NH_CARD"
  }
  /** 하나카드 */
  @SerialName("HANA_CARD")
  public data object HanaCard : PromotionCardCompany {
    override val value: String = "HANA_CARD"
  }
  /** 국민카드 */
  @SerialName("KOOKMIN_CARD")
  public data object KookminCard : PromotionCardCompany {
    override val value: String = "KOOKMIN_CARD"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PromotionCardCompany
}

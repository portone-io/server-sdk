package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 프로모션 적용 가능한 카드사 */
@Serializable(PromotionCardCompanySerializer::class)
public sealed interface PromotionCardCompany {
  public val value: String
  /** 우리카드 */
  public data object WooriCard : PromotionCardCompany {
    override val value: String = "WOORI_CARD"
  }
  /** BC카드 */
  public data object BcCard : PromotionCardCompany {
    override val value: String = "BC_CARD"
  }
  /** 삼성카드 */
  public data object SamsungCard : PromotionCardCompany {
    override val value: String = "SAMSUNG_CARD"
  }
  /** 신한카드 */
  public data object ShinhanCard : PromotionCardCompany {
    override val value: String = "SHINHAN_CARD"
  }
  /** 현대카드 */
  public data object HyundaiCard : PromotionCardCompany {
    override val value: String = "HYUNDAI_CARD"
  }
  /** 롯데카드 */
  public data object LotteCard : PromotionCardCompany {
    override val value: String = "LOTTE_CARD"
  }
  /** NH카드 */
  public data object NhCard : PromotionCardCompany {
    override val value: String = "NH_CARD"
  }
  /** 하나카드 */
  public data object HanaCard : PromotionCardCompany {
    override val value: String = "HANA_CARD"
  }
  /** 국민카드 */
  public data object KookminCard : PromotionCardCompany {
    override val value: String = "KOOKMIN_CARD"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PromotionCardCompany
}


private object PromotionCardCompanySerializer : KSerializer<PromotionCardCompany> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PromotionCardCompany::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PromotionCardCompany {
    val value = decoder.decodeString()
    return when (value) {
      "WOORI_CARD" -> PromotionCardCompany.WooriCard
      "BC_CARD" -> PromotionCardCompany.BcCard
      "SAMSUNG_CARD" -> PromotionCardCompany.SamsungCard
      "SHINHAN_CARD" -> PromotionCardCompany.ShinhanCard
      "HYUNDAI_CARD" -> PromotionCardCompany.HyundaiCard
      "LOTTE_CARD" -> PromotionCardCompany.LotteCard
      "NH_CARD" -> PromotionCardCompany.NhCard
      "HANA_CARD" -> PromotionCardCompany.HanaCard
      "KOOKMIN_CARD" -> PromotionCardCompany.KookminCard
      else -> PromotionCardCompany.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PromotionCardCompany) = encoder.encodeString(value.value)
}

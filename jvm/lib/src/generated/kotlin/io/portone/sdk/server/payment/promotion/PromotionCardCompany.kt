package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
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
  @Serializable(WooriCardSerializer::class)
  public data object WooriCard : PromotionCardCompany {
    override val value: String = "WOORI_CARD"
  }
  private object WooriCardSerializer : KSerializer<WooriCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(WooriCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): WooriCard = decoder.decodeString().let {
      if (it != "WOORI_CARD") {
        throw SerializationException(it)
      } else {
        return WooriCard
      }
    }
    override fun serialize(encoder: Encoder, value: WooriCard) = encoder.encodeString(value.value)
  }
  /** BC카드 */
  @Serializable(BcCardSerializer::class)
  public data object BcCard : PromotionCardCompany {
    override val value: String = "BC_CARD"
  }
  private object BcCardSerializer : KSerializer<BcCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BcCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BcCard = decoder.decodeString().let {
      if (it != "BC_CARD") {
        throw SerializationException(it)
      } else {
        return BcCard
      }
    }
    override fun serialize(encoder: Encoder, value: BcCard) = encoder.encodeString(value.value)
  }
  /** 삼성카드 */
  @Serializable(SamsungCardSerializer::class)
  public data object SamsungCard : PromotionCardCompany {
    override val value: String = "SAMSUNG_CARD"
  }
  private object SamsungCardSerializer : KSerializer<SamsungCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SamsungCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SamsungCard = decoder.decodeString().let {
      if (it != "SAMSUNG_CARD") {
        throw SerializationException(it)
      } else {
        return SamsungCard
      }
    }
    override fun serialize(encoder: Encoder, value: SamsungCard) = encoder.encodeString(value.value)
  }
  /** 신한카드 */
  @Serializable(ShinhanCardSerializer::class)
  public data object ShinhanCard : PromotionCardCompany {
    override val value: String = "SHINHAN_CARD"
  }
  private object ShinhanCardSerializer : KSerializer<ShinhanCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ShinhanCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ShinhanCard = decoder.decodeString().let {
      if (it != "SHINHAN_CARD") {
        throw SerializationException(it)
      } else {
        return ShinhanCard
      }
    }
    override fun serialize(encoder: Encoder, value: ShinhanCard) = encoder.encodeString(value.value)
  }
  /** 현대카드 */
  @Serializable(HyundaiCardSerializer::class)
  public data object HyundaiCard : PromotionCardCompany {
    override val value: String = "HYUNDAI_CARD"
  }
  private object HyundaiCardSerializer : KSerializer<HyundaiCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HyundaiCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HyundaiCard = decoder.decodeString().let {
      if (it != "HYUNDAI_CARD") {
        throw SerializationException(it)
      } else {
        return HyundaiCard
      }
    }
    override fun serialize(encoder: Encoder, value: HyundaiCard) = encoder.encodeString(value.value)
  }
  /** 롯데카드 */
  @Serializable(LotteCardSerializer::class)
  public data object LotteCard : PromotionCardCompany {
    override val value: String = "LOTTE_CARD"
  }
  private object LotteCardSerializer : KSerializer<LotteCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(LotteCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): LotteCard = decoder.decodeString().let {
      if (it != "LOTTE_CARD") {
        throw SerializationException(it)
      } else {
        return LotteCard
      }
    }
    override fun serialize(encoder: Encoder, value: LotteCard) = encoder.encodeString(value.value)
  }
  /** NH카드 */
  @Serializable(NhCardSerializer::class)
  public data object NhCard : PromotionCardCompany {
    override val value: String = "NH_CARD"
  }
  private object NhCardSerializer : KSerializer<NhCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NhCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NhCard = decoder.decodeString().let {
      if (it != "NH_CARD") {
        throw SerializationException(it)
      } else {
        return NhCard
      }
    }
    override fun serialize(encoder: Encoder, value: NhCard) = encoder.encodeString(value.value)
  }
  /** 하나카드 */
  @Serializable(HanaCardSerializer::class)
  public data object HanaCard : PromotionCardCompany {
    override val value: String = "HANA_CARD"
  }
  private object HanaCardSerializer : KSerializer<HanaCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HanaCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HanaCard = decoder.decodeString().let {
      if (it != "HANA_CARD") {
        throw SerializationException(it)
      } else {
        return HanaCard
      }
    }
    override fun serialize(encoder: Encoder, value: HanaCard) = encoder.encodeString(value.value)
  }
  /** 국민카드 */
  @Serializable(KookminCardSerializer::class)
  public data object KookminCard : PromotionCardCompany {
    override val value: String = "KOOKMIN_CARD"
  }
  private object KookminCardSerializer : KSerializer<KookminCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KookminCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KookminCard = decoder.decodeString().let {
      if (it != "KOOKMIN_CARD") {
        throw SerializationException(it)
      } else {
        return KookminCard
      }
    }
    override fun serialize(encoder: Encoder, value: KookminCard) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PromotionCardCompany
}


private object PromotionCardCompanySerializer : KSerializer<PromotionCardCompany> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PromotionCardCompany::class.java.name, PrimitiveKind.STRING)
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

package io.portone.sdk.server.payment.additionalfeature

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/**
 * PG 프로모션 카드사
 *
 * PG사 프로모션 조회 시 필터링할 수 있는 카드사 목록입니다.
 */
@Serializable(PgPromotionCardCompanySerializer::class)
public sealed interface PgPromotionCardCompany {
  public val value: String
  /** KDB산업은행 */
  @Serializable(KoreaDevelopmentBankSerializer::class)
  public data object KoreaDevelopmentBank : PgPromotionCardCompany {
    override val value: String = "KOREA_DEVELOPMENT_BANK"
  }
  public object KoreaDevelopmentBankSerializer : KSerializer<KoreaDevelopmentBank> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KoreaDevelopmentBank::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KoreaDevelopmentBank = decoder.decodeString().let {
      if (it != "KOREA_DEVELOPMENT_BANK") {
        throw SerializationException(it)
      } else {
        return KoreaDevelopmentBank
      }
    }
    override fun serialize(encoder: Encoder, value: KoreaDevelopmentBank): Unit = encoder.encodeString(value.value)
  }
  /** 새마을금고 */
  @Serializable(KfccSerializer::class)
  public data object Kfcc : PgPromotionCardCompany {
    override val value: String = "KFCC"
  }
  public object KfccSerializer : KSerializer<Kfcc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kfcc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kfcc = decoder.decodeString().let {
      if (it != "KFCC") {
        throw SerializationException(it)
      } else {
        return Kfcc
      }
    }
    override fun serialize(encoder: Encoder, value: Kfcc): Unit = encoder.encodeString(value.value)
  }
  /** 신협 */
  @Serializable(ShinhyupSerializer::class)
  public data object Shinhyup : PgPromotionCardCompany {
    override val value: String = "SHINHYUP"
  }
  public object ShinhyupSerializer : KSerializer<Shinhyup> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Shinhyup::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Shinhyup = decoder.decodeString().let {
      if (it != "SHINHYUP") {
        throw SerializationException(it)
      } else {
        return Shinhyup
      }
    }
    override fun serialize(encoder: Encoder, value: Shinhyup): Unit = encoder.encodeString(value.value)
  }
  /** 우체국 */
  @Serializable(EpostSerializer::class)
  public data object Epost : PgPromotionCardCompany {
    override val value: String = "EPOST"
  }
  public object EpostSerializer : KSerializer<Epost> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Epost::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Epost = decoder.decodeString().let {
      if (it != "EPOST") {
        throw SerializationException(it)
      } else {
        return Epost
      }
    }
    override fun serialize(encoder: Encoder, value: Epost): Unit = encoder.encodeString(value.value)
  }
  /** 저축은행 */
  @Serializable(SavingsBankKoreaSerializer::class)
  public data object SavingsBankKorea : PgPromotionCardCompany {
    override val value: String = "SAVINGS_BANK_KOREA"
  }
  public object SavingsBankKoreaSerializer : KSerializer<SavingsBankKorea> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SavingsBankKorea::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SavingsBankKorea = decoder.decodeString().let {
      if (it != "SAVINGS_BANK_KOREA") {
        throw SerializationException(it)
      } else {
        return SavingsBankKorea
      }
    }
    override fun serialize(encoder: Encoder, value: SavingsBankKorea): Unit = encoder.encodeString(value.value)
  }
  /** 카카오뱅크 */
  @Serializable(KakaoBankSerializer::class)
  public data object KakaoBank : PgPromotionCardCompany {
    override val value: String = "KAKAO_BANK"
  }
  public object KakaoBankSerializer : KSerializer<KakaoBank> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KakaoBank::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KakaoBank = decoder.decodeString().let {
      if (it != "KAKAO_BANK") {
        throw SerializationException(it)
      } else {
        return KakaoBank
      }
    }
    override fun serialize(encoder: Encoder, value: KakaoBank): Unit = encoder.encodeString(value.value)
  }
  /** 우리카드 */
  @Serializable(WooriCardSerializer::class)
  public data object WooriCard : PgPromotionCardCompany {
    override val value: String = "WOORI_CARD"
  }
  public object WooriCardSerializer : KSerializer<WooriCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(WooriCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): WooriCard = decoder.decodeString().let {
      if (it != "WOORI_CARD") {
        throw SerializationException(it)
      } else {
        return WooriCard
      }
    }
    override fun serialize(encoder: Encoder, value: WooriCard): Unit = encoder.encodeString(value.value)
  }
  /** BC카드 */
  @Serializable(BcCardSerializer::class)
  public data object BcCard : PgPromotionCardCompany {
    override val value: String = "BC_CARD"
  }
  public object BcCardSerializer : KSerializer<BcCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BcCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BcCard = decoder.decodeString().let {
      if (it != "BC_CARD") {
        throw SerializationException(it)
      } else {
        return BcCard
      }
    }
    override fun serialize(encoder: Encoder, value: BcCard): Unit = encoder.encodeString(value.value)
  }
  /** 광주카드 */
  @Serializable(GwangjuCardSerializer::class)
  public data object GwangjuCard : PgPromotionCardCompany {
    override val value: String = "GWANGJU_CARD"
  }
  public object GwangjuCardSerializer : KSerializer<GwangjuCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(GwangjuCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): GwangjuCard = decoder.decodeString().let {
      if (it != "GWANGJU_CARD") {
        throw SerializationException(it)
      } else {
        return GwangjuCard
      }
    }
    override fun serialize(encoder: Encoder, value: GwangjuCard): Unit = encoder.encodeString(value.value)
  }
  /** 삼성카드 */
  @Serializable(SamsungCardSerializer::class)
  public data object SamsungCard : PgPromotionCardCompany {
    override val value: String = "SAMSUNG_CARD"
  }
  public object SamsungCardSerializer : KSerializer<SamsungCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SamsungCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SamsungCard = decoder.decodeString().let {
      if (it != "SAMSUNG_CARD") {
        throw SerializationException(it)
      } else {
        return SamsungCard
      }
    }
    override fun serialize(encoder: Encoder, value: SamsungCard): Unit = encoder.encodeString(value.value)
  }
  /** 신한카드 */
  @Serializable(ShinhanCardSerializer::class)
  public data object ShinhanCard : PgPromotionCardCompany {
    override val value: String = "SHINHAN_CARD"
  }
  public object ShinhanCardSerializer : KSerializer<ShinhanCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ShinhanCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ShinhanCard = decoder.decodeString().let {
      if (it != "SHINHAN_CARD") {
        throw SerializationException(it)
      } else {
        return ShinhanCard
      }
    }
    override fun serialize(encoder: Encoder, value: ShinhanCard): Unit = encoder.encodeString(value.value)
  }
  /** 현대카드 */
  @Serializable(HyundaiCardSerializer::class)
  public data object HyundaiCard : PgPromotionCardCompany {
    override val value: String = "HYUNDAI_CARD"
  }
  public object HyundaiCardSerializer : KSerializer<HyundaiCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HyundaiCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HyundaiCard = decoder.decodeString().let {
      if (it != "HYUNDAI_CARD") {
        throw SerializationException(it)
      } else {
        return HyundaiCard
      }
    }
    override fun serialize(encoder: Encoder, value: HyundaiCard): Unit = encoder.encodeString(value.value)
  }
  /** 롯데카드 */
  @Serializable(LotteCardSerializer::class)
  public data object LotteCard : PgPromotionCardCompany {
    override val value: String = "LOTTE_CARD"
  }
  public object LotteCardSerializer : KSerializer<LotteCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(LotteCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): LotteCard = decoder.decodeString().let {
      if (it != "LOTTE_CARD") {
        throw SerializationException(it)
      } else {
        return LotteCard
      }
    }
    override fun serialize(encoder: Encoder, value: LotteCard): Unit = encoder.encodeString(value.value)
  }
  /** 수협카드 */
  @Serializable(SuhyupCardSerializer::class)
  public data object SuhyupCard : PgPromotionCardCompany {
    override val value: String = "SUHYUP_CARD"
  }
  public object SuhyupCardSerializer : KSerializer<SuhyupCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SuhyupCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SuhyupCard = decoder.decodeString().let {
      if (it != "SUHYUP_CARD") {
        throw SerializationException(it)
      } else {
        return SuhyupCard
      }
    }
    override fun serialize(encoder: Encoder, value: SuhyupCard): Unit = encoder.encodeString(value.value)
  }
  /** 씨티카드 */
  @Serializable(CitiCardSerializer::class)
  public data object CitiCard : PgPromotionCardCompany {
    override val value: String = "CITI_CARD"
  }
  public object CitiCardSerializer : KSerializer<CitiCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CitiCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CitiCard = decoder.decodeString().let {
      if (it != "CITI_CARD") {
        throw SerializationException(it)
      } else {
        return CitiCard
      }
    }
    override fun serialize(encoder: Encoder, value: CitiCard): Unit = encoder.encodeString(value.value)
  }
  /** NH카드 */
  @Serializable(NhCardSerializer::class)
  public data object NhCard : PgPromotionCardCompany {
    override val value: String = "NH_CARD"
  }
  public object NhCardSerializer : KSerializer<NhCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NhCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NhCard = decoder.decodeString().let {
      if (it != "NH_CARD") {
        throw SerializationException(it)
      } else {
        return NhCard
      }
    }
    override fun serialize(encoder: Encoder, value: NhCard): Unit = encoder.encodeString(value.value)
  }
  /** 전북카드 */
  @Serializable(JeonbukCardSerializer::class)
  public data object JeonbukCard : PgPromotionCardCompany {
    override val value: String = "JEONBUK_CARD"
  }
  public object JeonbukCardSerializer : KSerializer<JeonbukCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(JeonbukCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): JeonbukCard = decoder.decodeString().let {
      if (it != "JEONBUK_CARD") {
        throw SerializationException(it)
      } else {
        return JeonbukCard
      }
    }
    override fun serialize(encoder: Encoder, value: JeonbukCard): Unit = encoder.encodeString(value.value)
  }
  /** 제주카드 */
  @Serializable(JejuCardSerializer::class)
  public data object JejuCard : PgPromotionCardCompany {
    override val value: String = "JEJU_CARD"
  }
  public object JejuCardSerializer : KSerializer<JejuCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(JejuCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): JejuCard = decoder.decodeString().let {
      if (it != "JEJU_CARD") {
        throw SerializationException(it)
      } else {
        return JejuCard
      }
    }
    override fun serialize(encoder: Encoder, value: JejuCard): Unit = encoder.encodeString(value.value)
  }
  /** 하나카드 */
  @Serializable(HanaCardSerializer::class)
  public data object HanaCard : PgPromotionCardCompany {
    override val value: String = "HANA_CARD"
  }
  public object HanaCardSerializer : KSerializer<HanaCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HanaCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HanaCard = decoder.decodeString().let {
      if (it != "HANA_CARD") {
        throw SerializationException(it)
      } else {
        return HanaCard
      }
    }
    override fun serialize(encoder: Encoder, value: HanaCard): Unit = encoder.encodeString(value.value)
  }
  /** 국민카드 */
  @Serializable(KookminCardSerializer::class)
  public data object KookminCard : PgPromotionCardCompany {
    override val value: String = "KOOKMIN_CARD"
  }
  public object KookminCardSerializer : KSerializer<KookminCard> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KookminCard::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KookminCard = decoder.decodeString().let {
      if (it != "KOOKMIN_CARD") {
        throw SerializationException(it)
      } else {
        return KookminCard
      }
    }
    override fun serialize(encoder: Encoder, value: KookminCard): Unit = encoder.encodeString(value.value)
  }
  /** 케이뱅크 */
  @Serializable(KBankSerializer::class)
  public data object KBank : PgPromotionCardCompany {
    override val value: String = "K_BANK"
  }
  public object KBankSerializer : KSerializer<KBank> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KBank::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KBank = decoder.decodeString().let {
      if (it != "K_BANK") {
        throw SerializationException(it)
      } else {
        return KBank
      }
    }
    override fun serialize(encoder: Encoder, value: KBank): Unit = encoder.encodeString(value.value)
  }
  /** 토스뱅크 */
  @Serializable(TossBankSerializer::class)
  public data object TossBank : PgPromotionCardCompany {
    override val value: String = "TOSS_BANK"
  }
  public object TossBankSerializer : KSerializer<TossBank> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TossBank::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TossBank = decoder.decodeString().let {
      if (it != "TOSS_BANK") {
        throw SerializationException(it)
      } else {
        return TossBank
      }
    }
    override fun serialize(encoder: Encoder, value: TossBank): Unit = encoder.encodeString(value.value)
  }
  /** 미래에셋증권 */
  @Serializable(MiraeAssetSecuritiesSerializer::class)
  public data object MiraeAssetSecurities : PgPromotionCardCompany {
    override val value: String = "MIRAE_ASSET_SECURITIES"
  }
  public object MiraeAssetSecuritiesSerializer : KSerializer<MiraeAssetSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(MiraeAssetSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): MiraeAssetSecurities = decoder.decodeString().let {
      if (it != "MIRAE_ASSET_SECURITIES") {
        throw SerializationException(it)
      } else {
        return MiraeAssetSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: MiraeAssetSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PgPromotionCardCompany
}


public object PgPromotionCardCompanySerializer : KSerializer<PgPromotionCardCompany> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PgPromotionCardCompany::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PgPromotionCardCompany {
    val value = decoder.decodeString()
    return when (value) {
      "KOREA_DEVELOPMENT_BANK" -> PgPromotionCardCompany.KoreaDevelopmentBank
      "KFCC" -> PgPromotionCardCompany.Kfcc
      "SHINHYUP" -> PgPromotionCardCompany.Shinhyup
      "EPOST" -> PgPromotionCardCompany.Epost
      "SAVINGS_BANK_KOREA" -> PgPromotionCardCompany.SavingsBankKorea
      "KAKAO_BANK" -> PgPromotionCardCompany.KakaoBank
      "WOORI_CARD" -> PgPromotionCardCompany.WooriCard
      "BC_CARD" -> PgPromotionCardCompany.BcCard
      "GWANGJU_CARD" -> PgPromotionCardCompany.GwangjuCard
      "SAMSUNG_CARD" -> PgPromotionCardCompany.SamsungCard
      "SHINHAN_CARD" -> PgPromotionCardCompany.ShinhanCard
      "HYUNDAI_CARD" -> PgPromotionCardCompany.HyundaiCard
      "LOTTE_CARD" -> PgPromotionCardCompany.LotteCard
      "SUHYUP_CARD" -> PgPromotionCardCompany.SuhyupCard
      "CITI_CARD" -> PgPromotionCardCompany.CitiCard
      "NH_CARD" -> PgPromotionCardCompany.NhCard
      "JEONBUK_CARD" -> PgPromotionCardCompany.JeonbukCard
      "JEJU_CARD" -> PgPromotionCardCompany.JejuCard
      "HANA_CARD" -> PgPromotionCardCompany.HanaCard
      "KOOKMIN_CARD" -> PgPromotionCardCompany.KookminCard
      "K_BANK" -> PgPromotionCardCompany.KBank
      "TOSS_BANK" -> PgPromotionCardCompany.TossBank
      "MIRAE_ASSET_SECURITIES" -> PgPromotionCardCompany.MiraeAssetSecurities
      else -> PgPromotionCardCompany.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PgPromotionCardCompany): Unit = encoder.encodeString(value.value)
}

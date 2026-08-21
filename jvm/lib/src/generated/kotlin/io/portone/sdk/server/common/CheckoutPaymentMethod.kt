package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제 수단 */
@Serializable(CheckoutPaymentMethodSerializer::class)
public sealed interface CheckoutPaymentMethod {
  public val value: String
  @Serializable(CardKrSerializer::class)
  public data object CardKr : CheckoutPaymentMethod {
    override val value: String = "CARD_KR"
  }
  public object CardKrSerializer : KSerializer<CardKr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardKr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CardKr = decoder.decodeString().let {
      if (it != "CARD_KR") {
        throw SerializationException(it)
      } else {
        return CardKr
      }
    }
    override fun serialize(encoder: Encoder, value: CardKr): Unit = encoder.encodeString(value.value)
  }
  @Serializable(NPaySerializer::class)
  public data object NPay : CheckoutPaymentMethod {
    override val value: String = "N_PAY"
  }
  public object NPaySerializer : KSerializer<NPay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NPay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NPay = decoder.decodeString().let {
      if (it != "N_PAY") {
        throw SerializationException(it)
      } else {
        return NPay
      }
    }
    override fun serialize(encoder: Encoder, value: NPay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KakaoPaySerializer::class)
  public data object KakaoPay : CheckoutPaymentMethod {
    override val value: String = "KAKAO_PAY"
  }
  public object KakaoPaySerializer : KSerializer<KakaoPay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KakaoPay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KakaoPay = decoder.decodeString().let {
      if (it != "KAKAO_PAY") {
        throw SerializationException(it)
      } else {
        return KakaoPay
      }
    }
    override fun serialize(encoder: Encoder, value: KakaoPay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(TossPaySerializer::class)
  public data object TossPay : CheckoutPaymentMethod {
    override val value: String = "TOSS_PAY"
  }
  public object TossPaySerializer : KSerializer<TossPay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TossPay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TossPay = decoder.decodeString().let {
      if (it != "TOSS_PAY") {
        throw SerializationException(it)
      } else {
        return TossPay
      }
    }
    override fun serialize(encoder: Encoder, value: TossPay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(CardInternationalSerializer::class)
  public data object CardInternational : CheckoutPaymentMethod {
    override val value: String = "CARD_INTERNATIONAL"
  }
  public object CardInternationalSerializer : KSerializer<CardInternational> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardInternational::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CardInternational = decoder.decodeString().let {
      if (it != "CARD_INTERNATIONAL") {
        throw SerializationException(it)
      } else {
        return CardInternational
      }
    }
    override fun serialize(encoder: Encoder, value: CardInternational): Unit = encoder.encodeString(value.value)
  }
  @Serializable(PayPalSerializer::class)
  public data object PayPal : CheckoutPaymentMethod {
    override val value: String = "PAY_PAL"
  }
  public object PayPalSerializer : KSerializer<PayPal> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PayPal::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PayPal = decoder.decodeString().let {
      if (it != "PAY_PAL") {
        throw SerializationException(it)
      } else {
        return PayPal
      }
    }
    override fun serialize(encoder: Encoder, value: PayPal): Unit = encoder.encodeString(value.value)
  }
  @Serializable(UnionPaySerializer::class)
  public data object UnionPay : CheckoutPaymentMethod {
    override val value: String = "UNION_PAY"
  }
  public object UnionPaySerializer : KSerializer<UnionPay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(UnionPay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): UnionPay = decoder.decodeString().let {
      if (it != "UNION_PAY") {
        throw SerializationException(it)
      } else {
        return UnionPay
      }
    }
    override fun serialize(encoder: Encoder, value: UnionPay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(AlipayCnSerializer::class)
  public data object AlipayCn : CheckoutPaymentMethod {
    override val value: String = "ALIPAY_CN"
  }
  public object AlipayCnSerializer : KSerializer<AlipayCn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(AlipayCn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AlipayCn = decoder.decodeString().let {
      if (it != "ALIPAY_CN") {
        throw SerializationException(it)
      } else {
        return AlipayCn
      }
    }
    override fun serialize(encoder: Encoder, value: AlipayCn): Unit = encoder.encodeString(value.value)
  }
  @Serializable(AlipayHkSerializer::class)
  public data object AlipayHk : CheckoutPaymentMethod {
    override val value: String = "ALIPAY_HK"
  }
  public object AlipayHkSerializer : KSerializer<AlipayHk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(AlipayHk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AlipayHk = decoder.decodeString().let {
      if (it != "ALIPAY_HK") {
        throw SerializationException(it)
      } else {
        return AlipayHk
      }
    }
    override fun serialize(encoder: Encoder, value: AlipayHk): Unit = encoder.encodeString(value.value)
  }
  @Serializable(TrueMoneySerializer::class)
  public data object TrueMoney : CheckoutPaymentMethod {
    override val value: String = "TRUE_MONEY"
  }
  public object TrueMoneySerializer : KSerializer<TrueMoney> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TrueMoney::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TrueMoney = decoder.decodeString().let {
      if (it != "TRUE_MONEY") {
        throw SerializationException(it)
      } else {
        return TrueMoney
      }
    }
    override fun serialize(encoder: Encoder, value: TrueMoney): Unit = encoder.encodeString(value.value)
  }
  @Serializable(DanaSerializer::class)
  public data object Dana : CheckoutPaymentMethod {
    override val value: String = "DANA"
  }
  public object DanaSerializer : KSerializer<Dana> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dana::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dana = decoder.decodeString().let {
      if (it != "DANA") {
        throw SerializationException(it)
      } else {
        return Dana
      }
    }
    override fun serialize(encoder: Encoder, value: Dana): Unit = encoder.encodeString(value.value)
  }
  @Serializable(TouchNGoSerializer::class)
  public data object TouchNGo : CheckoutPaymentMethod {
    override val value: String = "TOUCH_N_GO"
  }
  public object TouchNGoSerializer : KSerializer<TouchNGo> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TouchNGo::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TouchNGo = decoder.decodeString().let {
      if (it != "TOUCH_N_GO") {
        throw SerializationException(it)
      } else {
        return TouchNGo
      }
    }
    override fun serialize(encoder: Encoder, value: TouchNGo): Unit = encoder.encodeString(value.value)
  }
  @Serializable(GCashSerializer::class)
  public data object GCash : CheckoutPaymentMethod {
    override val value: String = "G_CASH"
  }
  public object GCashSerializer : KSerializer<GCash> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(GCash::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): GCash = decoder.decodeString().let {
      if (it != "G_CASH") {
        throw SerializationException(it)
      } else {
        return GCash
      }
    }
    override fun serialize(encoder: Encoder, value: GCash): Unit = encoder.encodeString(value.value)
  }
  @Serializable(WeChatPaySerializer::class)
  public data object WeChatPay : CheckoutPaymentMethod {
    override val value: String = "WE_CHAT_PAY"
  }
  public object WeChatPaySerializer : KSerializer<WeChatPay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(WeChatPay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): WeChatPay = decoder.decodeString().let {
      if (it != "WE_CHAT_PAY") {
        throw SerializationException(it)
      } else {
        return WeChatPay
      }
    }
    override fun serialize(encoder: Encoder, value: WeChatPay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KlarnaSerializer::class)
  public data object Klarna : CheckoutPaymentMethod {
    override val value: String = "KLARNA"
  }
  public object KlarnaSerializer : KSerializer<Klarna> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Klarna::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Klarna = decoder.decodeString().let {
      if (it != "KLARNA") {
        throw SerializationException(it)
      } else {
        return Klarna
      }
    }
    override fun serialize(encoder: Encoder, value: Klarna): Unit = encoder.encodeString(value.value)
  }
  @Serializable(EContextSerializer::class)
  public data object EContext : CheckoutPaymentMethod {
    override val value: String = "E_CONTEXT"
  }
  public object EContextSerializer : KSerializer<EContext> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(EContext::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): EContext = decoder.decodeString().let {
      if (it != "E_CONTEXT") {
        throw SerializationException(it)
      } else {
        return EContext
      }
    }
    override fun serialize(encoder: Encoder, value: EContext): Unit = encoder.encodeString(value.value)
  }
  @Serializable(GrabPayMySerializer::class)
  public data object GrabPayMy : CheckoutPaymentMethod {
    override val value: String = "GRAB_PAY_MY"
  }
  public object GrabPayMySerializer : KSerializer<GrabPayMy> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(GrabPayMy::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): GrabPayMy = decoder.decodeString().let {
      if (it != "GRAB_PAY_MY") {
        throw SerializationException(it)
      } else {
        return GrabPayMy
      }
    }
    override fun serialize(encoder: Encoder, value: GrabPayMy): Unit = encoder.encodeString(value.value)
  }
  @Serializable(GrabPaySgSerializer::class)
  public data object GrabPaySg : CheckoutPaymentMethod {
    override val value: String = "GRAB_PAY_SG"
  }
  public object GrabPaySgSerializer : KSerializer<GrabPaySg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(GrabPaySg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): GrabPaySg = decoder.decodeString().let {
      if (it != "GRAB_PAY_SG") {
        throw SerializationException(it)
      } else {
        return GrabPaySg
      }
    }
    override fun serialize(encoder: Encoder, value: GrabPaySg): Unit = encoder.encodeString(value.value)
  }
  @Serializable(ShopeePayThSerializer::class)
  public data object ShopeePayTh : CheckoutPaymentMethod {
    override val value: String = "SHOPEE_PAY_TH"
  }
  public object ShopeePayThSerializer : KSerializer<ShopeePayTh> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ShopeePayTh::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ShopeePayTh = decoder.decodeString().let {
      if (it != "SHOPEE_PAY_TH") {
        throw SerializationException(it)
      } else {
        return ShopeePayTh
      }
    }
    override fun serialize(encoder: Encoder, value: ShopeePayTh): Unit = encoder.encodeString(value.value)
  }
  @Serializable(PayPaySerializer::class)
  public data object PayPay : CheckoutPaymentMethod {
    override val value: String = "PAY_PAY"
  }
  public object PayPaySerializer : KSerializer<PayPay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PayPay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PayPay = decoder.decodeString().let {
      if (it != "PAY_PAY") {
        throw SerializationException(it)
      } else {
        return PayPay
      }
    }
    override fun serialize(encoder: Encoder, value: PayPay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(BpiSerializer::class)
  public data object Bpi : CheckoutPaymentMethod {
    override val value: String = "BPI"
  }
  public object BpiSerializer : KSerializer<Bpi> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bpi::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bpi = decoder.decodeString().let {
      if (it != "BPI") {
        throw SerializationException(it)
      } else {
        return Bpi
      }
    }
    override fun serialize(encoder: Encoder, value: Bpi): Unit = encoder.encodeString(value.value)
  }
  @Serializable(RabbitLinePaySerializer::class)
  public data object RabbitLinePay : CheckoutPaymentMethod {
    override val value: String = "RABBIT_LINE_PAY"
  }
  public object RabbitLinePaySerializer : KSerializer<RabbitLinePay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(RabbitLinePay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): RabbitLinePay = decoder.decodeString().let {
      if (it != "RABBIT_LINE_PAY") {
        throw SerializationException(it)
      } else {
        return RabbitLinePay
      }
    }
    override fun serialize(encoder: Encoder, value: RabbitLinePay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(ConvenienceStoreJpSerializer::class)
  public data object ConvenienceStoreJp : CheckoutPaymentMethod {
    override val value: String = "CONVENIENCE_STORE_JP"
  }
  public object ConvenienceStoreJpSerializer : KSerializer<ConvenienceStoreJp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ConvenienceStoreJp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ConvenienceStoreJp = decoder.decodeString().let {
      if (it != "CONVENIENCE_STORE_JP") {
        throw SerializationException(it)
      } else {
        return ConvenienceStoreJp
      }
    }
    override fun serialize(encoder: Encoder, value: ConvenienceStoreJp): Unit = encoder.encodeString(value.value)
  }
  @Serializable(AmazonPaySerializer::class)
  public data object AmazonPay : CheckoutPaymentMethod {
    override val value: String = "AMAZON_PAY"
  }
  public object AmazonPaySerializer : KSerializer<AmazonPay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(AmazonPay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AmazonPay = decoder.decodeString().let {
      if (it != "AMAZON_PAY") {
        throw SerializationException(it)
      } else {
        return AmazonPay
      }
    }
    override fun serialize(encoder: Encoder, value: AmazonPay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(RakutenPaySerializer::class)
  public data object RakutenPay : CheckoutPaymentMethod {
    override val value: String = "RAKUTEN_PAY"
  }
  public object RakutenPaySerializer : KSerializer<RakutenPay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(RakutenPay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): RakutenPay = decoder.decodeString().let {
      if (it != "RAKUTEN_PAY") {
        throw SerializationException(it)
      } else {
        return RakutenPay
      }
    }
    override fun serialize(encoder: Encoder, value: RakutenPay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(DBaraiSerializer::class)
  public data object DBarai : CheckoutPaymentMethod {
    override val value: String = "D_BARAI"
  }
  public object DBaraiSerializer : KSerializer<DBarai> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DBarai::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DBarai = decoder.decodeString().let {
      if (it != "D_BARAI") {
        throw SerializationException(it)
      } else {
        return DBarai
      }
    }
    override fun serialize(encoder: Encoder, value: DBarai): Unit = encoder.encodeString(value.value)
  }
  @Serializable(AuPaySerializer::class)
  public data object AuPay : CheckoutPaymentMethod {
    override val value: String = "AU_PAY"
  }
  public object AuPaySerializer : KSerializer<AuPay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(AuPay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AuPay = decoder.decodeString().let {
      if (it != "AU_PAY") {
        throw SerializationException(it)
      } else {
        return AuPay
      }
    }
    override fun serialize(encoder: Encoder, value: AuPay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(MerpaySerializer::class)
  public data object Merpay : CheckoutPaymentMethod {
    override val value: String = "MERPAY"
  }
  public object MerpaySerializer : KSerializer<Merpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Merpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Merpay = decoder.decodeString().let {
      if (it != "MERPAY") {
        throw SerializationException(it)
      } else {
        return Merpay
      }
    }
    override fun serialize(encoder: Encoder, value: Merpay): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CheckoutPaymentMethod
}


public object CheckoutPaymentMethodSerializer : KSerializer<CheckoutPaymentMethod> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CheckoutPaymentMethod::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CheckoutPaymentMethod {
    val value = decoder.decodeString()
    return when (value) {
      "CARD_KR" -> CheckoutPaymentMethod.CardKr
      "N_PAY" -> CheckoutPaymentMethod.NPay
      "KAKAO_PAY" -> CheckoutPaymentMethod.KakaoPay
      "TOSS_PAY" -> CheckoutPaymentMethod.TossPay
      "CARD_INTERNATIONAL" -> CheckoutPaymentMethod.CardInternational
      "PAY_PAL" -> CheckoutPaymentMethod.PayPal
      "UNION_PAY" -> CheckoutPaymentMethod.UnionPay
      "ALIPAY_CN" -> CheckoutPaymentMethod.AlipayCn
      "ALIPAY_HK" -> CheckoutPaymentMethod.AlipayHk
      "TRUE_MONEY" -> CheckoutPaymentMethod.TrueMoney
      "DANA" -> CheckoutPaymentMethod.Dana
      "TOUCH_N_GO" -> CheckoutPaymentMethod.TouchNGo
      "G_CASH" -> CheckoutPaymentMethod.GCash
      "WE_CHAT_PAY" -> CheckoutPaymentMethod.WeChatPay
      "KLARNA" -> CheckoutPaymentMethod.Klarna
      "E_CONTEXT" -> CheckoutPaymentMethod.EContext
      "GRAB_PAY_MY" -> CheckoutPaymentMethod.GrabPayMy
      "GRAB_PAY_SG" -> CheckoutPaymentMethod.GrabPaySg
      "SHOPEE_PAY_TH" -> CheckoutPaymentMethod.ShopeePayTh
      "PAY_PAY" -> CheckoutPaymentMethod.PayPay
      "BPI" -> CheckoutPaymentMethod.Bpi
      "RABBIT_LINE_PAY" -> CheckoutPaymentMethod.RabbitLinePay
      "CONVENIENCE_STORE_JP" -> CheckoutPaymentMethod.ConvenienceStoreJp
      "AMAZON_PAY" -> CheckoutPaymentMethod.AmazonPay
      "RAKUTEN_PAY" -> CheckoutPaymentMethod.RakutenPay
      "D_BARAI" -> CheckoutPaymentMethod.DBarai
      "AU_PAY" -> CheckoutPaymentMethod.AuPay
      "MERPAY" -> CheckoutPaymentMethod.Merpay
      else -> CheckoutPaymentMethod.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CheckoutPaymentMethod): Unit = encoder.encodeString(value.value)
}

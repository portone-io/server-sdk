package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 간편 결제사 */
@Serializable(EasyPayProviderSerializer::class)
public sealed interface EasyPayProvider {
  public val value: String
  @Serializable(SamsungpaySerializer::class)
  public data object Samsungpay : EasyPayProvider {
    override val value: String = "SAMSUNGPAY"
  }
  public object SamsungpaySerializer : KSerializer<Samsungpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Samsungpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Samsungpay = decoder.decodeString().let {
      if (it != "SAMSUNGPAY") {
        throw SerializationException(it)
      } else {
        return Samsungpay
      }
    }
    override fun serialize(encoder: Encoder, value: Samsungpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KakaopaySerializer::class)
  public data object Kakaopay : EasyPayProvider {
    override val value: String = "KAKAOPAY"
  }
  public object KakaopaySerializer : KSerializer<Kakaopay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kakaopay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kakaopay = decoder.decodeString().let {
      if (it != "KAKAOPAY") {
        throw SerializationException(it)
      } else {
        return Kakaopay
      }
    }
    override fun serialize(encoder: Encoder, value: Kakaopay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(NaverpaySerializer::class)
  public data object Naverpay : EasyPayProvider {
    override val value: String = "NAVERPAY"
  }
  public object NaverpaySerializer : KSerializer<Naverpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Naverpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Naverpay = decoder.decodeString().let {
      if (it != "NAVERPAY") {
        throw SerializationException(it)
      } else {
        return Naverpay
      }
    }
    override fun serialize(encoder: Encoder, value: Naverpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(PaycoSerializer::class)
  public data object Payco : EasyPayProvider {
    override val value: String = "PAYCO"
  }
  public object PaycoSerializer : KSerializer<Payco> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Payco::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Payco = decoder.decodeString().let {
      if (it != "PAYCO") {
        throw SerializationException(it)
      } else {
        return Payco
      }
    }
    override fun serialize(encoder: Encoder, value: Payco): Unit = encoder.encodeString(value.value)
  }
  @Serializable(SsgpaySerializer::class)
  public data object Ssgpay : EasyPayProvider {
    override val value: String = "SSGPAY"
  }
  public object SsgpaySerializer : KSerializer<Ssgpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ssgpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ssgpay = decoder.decodeString().let {
      if (it != "SSGPAY") {
        throw SerializationException(it)
      } else {
        return Ssgpay
      }
    }
    override fun serialize(encoder: Encoder, value: Ssgpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(ChaiSerializer::class)
  public data object Chai : EasyPayProvider {
    override val value: String = "CHAI"
  }
  public object ChaiSerializer : KSerializer<Chai> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Chai::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Chai = decoder.decodeString().let {
      if (it != "CHAI") {
        throw SerializationException(it)
      } else {
        return Chai
      }
    }
    override fun serialize(encoder: Encoder, value: Chai): Unit = encoder.encodeString(value.value)
  }
  @Serializable(LpaySerializer::class)
  public data object Lpay : EasyPayProvider {
    override val value: String = "LPAY"
  }
  public object LpaySerializer : KSerializer<Lpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lpay = decoder.decodeString().let {
      if (it != "LPAY") {
        throw SerializationException(it)
      } else {
        return Lpay
      }
    }
    override fun serialize(encoder: Encoder, value: Lpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KpaySerializer::class)
  public data object Kpay : EasyPayProvider {
    override val value: String = "KPAY"
  }
  public object KpaySerializer : KSerializer<Kpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kpay = decoder.decodeString().let {
      if (it != "KPAY") {
        throw SerializationException(it)
      } else {
        return Kpay
      }
    }
    override fun serialize(encoder: Encoder, value: Kpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(TosspaySerializer::class)
  public data object Tosspay : EasyPayProvider {
    override val value: String = "TOSSPAY"
  }
  public object TosspaySerializer : KSerializer<Tosspay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tosspay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tosspay = decoder.decodeString().let {
      if (it != "TOSSPAY") {
        throw SerializationException(it)
      } else {
        return Tosspay
      }
    }
    override fun serialize(encoder: Encoder, value: Tosspay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(LgpaySerializer::class)
  public data object Lgpay : EasyPayProvider {
    override val value: String = "LGPAY"
  }
  public object LgpaySerializer : KSerializer<Lgpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lgpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lgpay = decoder.decodeString().let {
      if (it != "LGPAY") {
        throw SerializationException(it)
      } else {
        return Lgpay
      }
    }
    override fun serialize(encoder: Encoder, value: Lgpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(PinpaySerializer::class)
  public data object Pinpay : EasyPayProvider {
    override val value: String = "PINPAY"
  }
  public object PinpaySerializer : KSerializer<Pinpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pinpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pinpay = decoder.decodeString().let {
      if (it != "PINPAY") {
        throw SerializationException(it)
      } else {
        return Pinpay
      }
    }
    override fun serialize(encoder: Encoder, value: Pinpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(ApplepaySerializer::class)
  public data object Applepay : EasyPayProvider {
    override val value: String = "APPLEPAY"
  }
  public object ApplepaySerializer : KSerializer<Applepay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Applepay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Applepay = decoder.decodeString().let {
      if (it != "APPLEPAY") {
        throw SerializationException(it)
      } else {
        return Applepay
      }
    }
    override fun serialize(encoder: Encoder, value: Applepay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(SkpaySerializer::class)
  public data object Skpay : EasyPayProvider {
    override val value: String = "SKPAY"
  }
  public object SkpaySerializer : KSerializer<Skpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Skpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Skpay = decoder.decodeString().let {
      if (it != "SKPAY") {
        throw SerializationException(it)
      } else {
        return Skpay
      }
    }
    override fun serialize(encoder: Encoder, value: Skpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(TossBrandpaySerializer::class)
  public data object TossBrandpay : EasyPayProvider {
    override val value: String = "TOSS_BRANDPAY"
  }
  public object TossBrandpaySerializer : KSerializer<TossBrandpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TossBrandpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TossBrandpay = decoder.decodeString().let {
      if (it != "TOSS_BRANDPAY") {
        throw SerializationException(it)
      } else {
        return TossBrandpay
      }
    }
    override fun serialize(encoder: Encoder, value: TossBrandpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KbAppSerializer::class)
  public data object KbApp : EasyPayProvider {
    override val value: String = "KB_APP"
  }
  public object KbAppSerializer : KSerializer<KbApp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KbApp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KbApp = decoder.decodeString().let {
      if (it != "KB_APP") {
        throw SerializationException(it)
      } else {
        return KbApp
      }
    }
    override fun serialize(encoder: Encoder, value: KbApp): Unit = encoder.encodeString(value.value)
  }
  @Serializable(AlipaySerializer::class)
  public data object Alipay : EasyPayProvider {
    override val value: String = "ALIPAY"
  }
  public object AlipaySerializer : KSerializer<Alipay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Alipay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Alipay = decoder.decodeString().let {
      if (it != "ALIPAY") {
        throw SerializationException(it)
      } else {
        return Alipay
      }
    }
    override fun serialize(encoder: Encoder, value: Alipay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(HyphenSerializer::class)
  public data object Hyphen : EasyPayProvider {
    override val value: String = "HYPHEN"
  }
  public object HyphenSerializer : KSerializer<Hyphen> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hyphen::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hyphen = decoder.decodeString().let {
      if (it != "HYPHEN") {
        throw SerializationException(it)
      } else {
        return Hyphen
      }
    }
    override fun serialize(encoder: Encoder, value: Hyphen): Unit = encoder.encodeString(value.value)
  }
  @Serializable(TmoneySerializer::class)
  public data object Tmoney : EasyPayProvider {
    override val value: String = "TMONEY"
  }
  public object TmoneySerializer : KSerializer<Tmoney> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tmoney::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tmoney = decoder.decodeString().let {
      if (it != "TMONEY") {
        throw SerializationException(it)
      } else {
        return Tmoney
      }
    }
    override fun serialize(encoder: Encoder, value: Tmoney): Unit = encoder.encodeString(value.value)
  }
  @Serializable(PaypalSerializer::class)
  public data object Paypal : EasyPayProvider {
    override val value: String = "PAYPAL"
  }
  public object PaypalSerializer : KSerializer<Paypal> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Paypal::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Paypal = decoder.decodeString().let {
      if (it != "PAYPAL") {
        throw SerializationException(it)
      } else {
        return Paypal
      }
    }
    override fun serialize(encoder: Encoder, value: Paypal): Unit = encoder.encodeString(value.value)
  }
  @Serializable(SmilepaySerializer::class)
  public data object Smilepay : EasyPayProvider {
    override val value: String = "SMILEPAY"
  }
  public object SmilepaySerializer : KSerializer<Smilepay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Smilepay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Smilepay = decoder.decodeString().let {
      if (it != "SMILEPAY") {
        throw SerializationException(it)
      } else {
        return Smilepay
      }
    }
    override fun serialize(encoder: Encoder, value: Smilepay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(MirSerializer::class)
  public data object Mir : EasyPayProvider {
    override val value: String = "MIR"
  }
  public object MirSerializer : KSerializer<Mir> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mir::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mir = decoder.decodeString().let {
      if (it != "MIR") {
        throw SerializationException(it)
      } else {
        return Mir
      }
    }
    override fun serialize(encoder: Encoder, value: Mir): Unit = encoder.encodeString(value.value)
  }
  @Serializable(WechatSerializer::class)
  public data object Wechat : EasyPayProvider {
    override val value: String = "WECHAT"
  }
  public object WechatSerializer : KSerializer<Wechat> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Wechat::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Wechat = decoder.decodeString().let {
      if (it != "WECHAT") {
        throw SerializationException(it)
      } else {
        return Wechat
      }
    }
    override fun serialize(encoder: Encoder, value: Wechat): Unit = encoder.encodeString(value.value)
  }
  @Serializable(LinepaySerializer::class)
  public data object Linepay : EasyPayProvider {
    override val value: String = "LINEPAY"
  }
  public object LinepaySerializer : KSerializer<Linepay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Linepay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Linepay = decoder.decodeString().let {
      if (it != "LINEPAY") {
        throw SerializationException(it)
      } else {
        return Linepay
      }
    }
    override fun serialize(encoder: Encoder, value: Linepay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KlarnaSerializer::class)
  public data object Klarna : EasyPayProvider {
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
  @Serializable(GrabpaySerializer::class)
  public data object Grabpay : EasyPayProvider {
    override val value: String = "GRABPAY"
  }
  public object GrabpaySerializer : KSerializer<Grabpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Grabpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Grabpay = decoder.decodeString().let {
      if (it != "GRABPAY") {
        throw SerializationException(it)
      } else {
        return Grabpay
      }
    }
    override fun serialize(encoder: Encoder, value: Grabpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(ShopeepaySerializer::class)
  public data object Shopeepay : EasyPayProvider {
    override val value: String = "SHOPEEPAY"
  }
  public object ShopeepaySerializer : KSerializer<Shopeepay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Shopeepay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Shopeepay = decoder.decodeString().let {
      if (it != "SHOPEEPAY") {
        throw SerializationException(it)
      } else {
        return Shopeepay
      }
    }
    override fun serialize(encoder: Encoder, value: Shopeepay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(JkopaySerializer::class)
  public data object Jkopay : EasyPayProvider {
    override val value: String = "JKOPAY"
  }
  public object JkopaySerializer : KSerializer<Jkopay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jkopay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jkopay = decoder.decodeString().let {
      if (it != "JKOPAY") {
        throw SerializationException(it)
      } else {
        return Jkopay
      }
    }
    override fun serialize(encoder: Encoder, value: Jkopay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(PaypaySerializer::class)
  public data object Paypay : EasyPayProvider {
    override val value: String = "PAYPAY"
  }
  public object PaypaySerializer : KSerializer<Paypay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Paypay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Paypay = decoder.decodeString().let {
      if (it != "PAYPAY") {
        throw SerializationException(it)
      } else {
        return Paypay
      }
    }
    override fun serialize(encoder: Encoder, value: Paypay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(AmazonpaySerializer::class)
  public data object Amazonpay : EasyPayProvider {
    override val value: String = "AMAZONPAY"
  }
  public object AmazonpaySerializer : KSerializer<Amazonpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Amazonpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Amazonpay = decoder.decodeString().let {
      if (it != "AMAZONPAY") {
        throw SerializationException(it)
      } else {
        return Amazonpay
      }
    }
    override fun serialize(encoder: Encoder, value: Amazonpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(RakutenpaySerializer::class)
  public data object Rakutenpay : EasyPayProvider {
    override val value: String = "RAKUTENPAY"
  }
  public object RakutenpaySerializer : KSerializer<Rakutenpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Rakutenpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Rakutenpay = decoder.decodeString().let {
      if (it != "RAKUTENPAY") {
        throw SerializationException(it)
      } else {
        return Rakutenpay
      }
    }
    override fun serialize(encoder: Encoder, value: Rakutenpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(DbaraiSerializer::class)
  public data object Dbarai : EasyPayProvider {
    override val value: String = "DBARAI"
  }
  public object DbaraiSerializer : KSerializer<Dbarai> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dbarai::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dbarai = decoder.decodeString().let {
      if (it != "DBARAI") {
        throw SerializationException(it)
      } else {
        return Dbarai
      }
    }
    override fun serialize(encoder: Encoder, value: Dbarai): Unit = encoder.encodeString(value.value)
  }
  @Serializable(AupaySerializer::class)
  public data object Aupay : EasyPayProvider {
    override val value: String = "AUPAY"
  }
  public object AupaySerializer : KSerializer<Aupay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Aupay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Aupay = decoder.decodeString().let {
      if (it != "AUPAY") {
        throw SerializationException(it)
      } else {
        return Aupay
      }
    }
    override fun serialize(encoder: Encoder, value: Aupay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(MerpaySerializer::class)
  public data object Merpay : EasyPayProvider {
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
  @Serializable(MoneytreeSerializer::class)
  public data object Moneytree : EasyPayProvider {
    override val value: String = "MONEYTREE"
  }
  public object MoneytreeSerializer : KSerializer<Moneytree> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Moneytree::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Moneytree = decoder.decodeString().let {
      if (it != "MONEYTREE") {
        throw SerializationException(it)
      } else {
        return Moneytree
      }
    }
    override fun serialize(encoder: Encoder, value: Moneytree): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KplusSerializer::class)
  public data object Kplus : EasyPayProvider {
    override val value: String = "KPLUS"
  }
  public object KplusSerializer : KSerializer<Kplus> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kplus::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kplus = decoder.decodeString().let {
      if (it != "KPLUS") {
        throw SerializationException(it)
      } else {
        return Kplus
      }
    }
    override fun serialize(encoder: Encoder, value: Kplus): Unit = encoder.encodeString(value.value)
  }
  @Serializable(TinabaSerializer::class)
  public data object Tinaba : EasyPayProvider {
    override val value: String = "TINABA"
  }
  public object TinabaSerializer : KSerializer<Tinaba> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tinaba::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tinaba = decoder.decodeString().let {
      if (it != "TINABA") {
        throw SerializationException(it)
      } else {
        return Tinaba
      }
    }
    override fun serialize(encoder: Encoder, value: Tinaba): Unit = encoder.encodeString(value.value)
  }
  @Serializable(BillEaseSerializer::class)
  public data object BillEase : EasyPayProvider {
    override val value: String = "BILL_EASE"
  }
  public object BillEaseSerializer : KSerializer<BillEase> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BillEase::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BillEase = decoder.decodeString().let {
      if (it != "BILL_EASE") {
        throw SerializationException(it)
      } else {
        return BillEase
      }
    }
    override fun serialize(encoder: Encoder, value: BillEase): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KredivoSerializer::class)
  public data object Kredivo : EasyPayProvider {
    override val value: String = "KREDIVO"
  }
  public object KredivoSerializer : KSerializer<Kredivo> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kredivo::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kredivo = decoder.decodeString().let {
      if (it != "KREDIVO") {
        throw SerializationException(it)
      } else {
        return Kredivo
      }
    }
    override fun serialize(encoder: Encoder, value: Kredivo): Unit = encoder.encodeString(value.value)
  }
  @Serializable(RabbitLinePaySerializer::class)
  public data object RabbitLinePay : EasyPayProvider {
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
  @Serializable(AlipayHkSerializer::class)
  public data object AlipayHk : EasyPayProvider {
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
  @Serializable(AkulakuPayLaterSerializer::class)
  public data object AkulakuPayLater : EasyPayProvider {
    override val value: String = "AKULAKU_PAY_LATER"
  }
  public object AkulakuPayLaterSerializer : KSerializer<AkulakuPayLater> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(AkulakuPayLater::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AkulakuPayLater = decoder.decodeString().let {
      if (it != "AKULAKU_PAY_LATER") {
        throw SerializationException(it)
      } else {
        return AkulakuPayLater
      }
    }
    override fun serialize(encoder: Encoder, value: AkulakuPayLater): Unit = encoder.encodeString(value.value)
  }
  @Serializable(BoostSerializer::class)
  public data object Boost : EasyPayProvider {
    override val value: String = "BOOST"
  }
  public object BoostSerializer : KSerializer<Boost> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Boost::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Boost = decoder.decodeString().let {
      if (it != "BOOST") {
        throw SerializationException(it)
      } else {
        return Boost
      }
    }
    override fun serialize(encoder: Encoder, value: Boost): Unit = encoder.encodeString(value.value)
  }
  @Serializable(BpiSerializer::class)
  public data object Bpi : EasyPayProvider {
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
  @Serializable(DanaSerializer::class)
  public data object Dana : EasyPayProvider {
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
  @Serializable(GCashSerializer::class)
  public data object GCash : EasyPayProvider {
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
  @Serializable(HipaySerializer::class)
  public data object Hipay : EasyPayProvider {
    override val value: String = "HIPAY"
  }
  public object HipaySerializer : KSerializer<Hipay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hipay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hipay = decoder.decodeString().let {
      if (it != "HIPAY") {
        throw SerializationException(it)
      } else {
        return Hipay
      }
    }
    override fun serialize(encoder: Encoder, value: Hipay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(MpaySerializer::class)
  public data object Mpay : EasyPayProvider {
    override val value: String = "MPAY"
  }
  public object MpaySerializer : KSerializer<Mpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mpay = decoder.decodeString().let {
      if (it != "MPAY") {
        throw SerializationException(it)
      } else {
        return Mpay
      }
    }
    override fun serialize(encoder: Encoder, value: Mpay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(TouchNGoSerializer::class)
  public data object TouchNGo : EasyPayProvider {
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
  @Serializable(TrueMoneySerializer::class)
  public data object TrueMoney : EasyPayProvider {
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
  @Serializable(DokuWalletSerializer::class)
  public data object DokuWallet : EasyPayProvider {
    override val value: String = "DOKU_WALLET"
  }
  public object DokuWalletSerializer : KSerializer<DokuWallet> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DokuWallet::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DokuWallet = decoder.decodeString().let {
      if (it != "DOKU_WALLET") {
        throw SerializationException(it)
      } else {
        return DokuWallet
      }
    }
    override fun serialize(encoder: Encoder, value: DokuWallet): Unit = encoder.encodeString(value.value)
  }
  @Serializable(JeniusPaySerializer::class)
  public data object JeniusPay : EasyPayProvider {
    override val value: String = "JENIUS_PAY"
  }
  public object JeniusPaySerializer : KSerializer<JeniusPay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(JeniusPay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): JeniusPay = decoder.decodeString().let {
      if (it != "JENIUS_PAY") {
        throw SerializationException(it)
      } else {
        return JeniusPay
      }
    }
    override fun serialize(encoder: Encoder, value: JeniusPay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(OvoSerializer::class)
  public data object Ovo : EasyPayProvider {
    override val value: String = "OVO"
  }
  public object OvoSerializer : KSerializer<Ovo> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ovo::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ovo = decoder.decodeString().let {
      if (it != "OVO") {
        throw SerializationException(it)
      } else {
        return Ovo
      }
    }
    override fun serialize(encoder: Encoder, value: Ovo): Unit = encoder.encodeString(value.value)
  }
  @Serializable(MayaSerializer::class)
  public data object Maya : EasyPayProvider {
    override val value: String = "MAYA"
  }
  public object MayaSerializer : KSerializer<Maya> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Maya::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Maya = decoder.decodeString().let {
      if (it != "MAYA") {
        throw SerializationException(it)
      } else {
        return Maya
      }
    }
    override fun serialize(encoder: Encoder, value: Maya): Unit = encoder.encodeString(value.value)
  }
  @Serializable(QrisSerializer::class)
  public data object Qris : EasyPayProvider {
    override val value: String = "QRIS"
  }
  public object QrisSerializer : KSerializer<Qris> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Qris::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Qris = decoder.decodeString().let {
      if (it != "QRIS") {
        throw SerializationException(it)
      } else {
        return Qris
      }
    }
    override fun serialize(encoder: Encoder, value: Qris): Unit = encoder.encodeString(value.value)
  }
  @Serializable(ThaiQrSerializer::class)
  public data object ThaiQr : EasyPayProvider {
    override val value: String = "THAI_QR"
  }
  public object ThaiQrSerializer : KSerializer<ThaiQr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ThaiQr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ThaiQr = decoder.decodeString().let {
      if (it != "THAI_QR") {
        throw SerializationException(it)
      } else {
        return ThaiQr
      }
    }
    override fun serialize(encoder: Encoder, value: ThaiQr): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : EasyPayProvider
}


public object EasyPayProviderSerializer : KSerializer<EasyPayProvider> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(EasyPayProvider::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): EasyPayProvider {
    val value = decoder.decodeString()
    return when (value) {
      "SAMSUNGPAY" -> EasyPayProvider.Samsungpay
      "KAKAOPAY" -> EasyPayProvider.Kakaopay
      "NAVERPAY" -> EasyPayProvider.Naverpay
      "PAYCO" -> EasyPayProvider.Payco
      "SSGPAY" -> EasyPayProvider.Ssgpay
      "CHAI" -> EasyPayProvider.Chai
      "LPAY" -> EasyPayProvider.Lpay
      "KPAY" -> EasyPayProvider.Kpay
      "TOSSPAY" -> EasyPayProvider.Tosspay
      "LGPAY" -> EasyPayProvider.Lgpay
      "PINPAY" -> EasyPayProvider.Pinpay
      "APPLEPAY" -> EasyPayProvider.Applepay
      "SKPAY" -> EasyPayProvider.Skpay
      "TOSS_BRANDPAY" -> EasyPayProvider.TossBrandpay
      "KB_APP" -> EasyPayProvider.KbApp
      "ALIPAY" -> EasyPayProvider.Alipay
      "HYPHEN" -> EasyPayProvider.Hyphen
      "TMONEY" -> EasyPayProvider.Tmoney
      "PAYPAL" -> EasyPayProvider.Paypal
      "SMILEPAY" -> EasyPayProvider.Smilepay
      "MIR" -> EasyPayProvider.Mir
      "WECHAT" -> EasyPayProvider.Wechat
      "LINEPAY" -> EasyPayProvider.Linepay
      "KLARNA" -> EasyPayProvider.Klarna
      "GRABPAY" -> EasyPayProvider.Grabpay
      "SHOPEEPAY" -> EasyPayProvider.Shopeepay
      "JKOPAY" -> EasyPayProvider.Jkopay
      "PAYPAY" -> EasyPayProvider.Paypay
      "AMAZONPAY" -> EasyPayProvider.Amazonpay
      "RAKUTENPAY" -> EasyPayProvider.Rakutenpay
      "DBARAI" -> EasyPayProvider.Dbarai
      "AUPAY" -> EasyPayProvider.Aupay
      "MERPAY" -> EasyPayProvider.Merpay
      "MONEYTREE" -> EasyPayProvider.Moneytree
      "KPLUS" -> EasyPayProvider.Kplus
      "TINABA" -> EasyPayProvider.Tinaba
      "BILL_EASE" -> EasyPayProvider.BillEase
      "KREDIVO" -> EasyPayProvider.Kredivo
      "RABBIT_LINE_PAY" -> EasyPayProvider.RabbitLinePay
      "ALIPAY_HK" -> EasyPayProvider.AlipayHk
      "AKULAKU_PAY_LATER" -> EasyPayProvider.AkulakuPayLater
      "BOOST" -> EasyPayProvider.Boost
      "BPI" -> EasyPayProvider.Bpi
      "DANA" -> EasyPayProvider.Dana
      "G_CASH" -> EasyPayProvider.GCash
      "HIPAY" -> EasyPayProvider.Hipay
      "MPAY" -> EasyPayProvider.Mpay
      "TOUCH_N_GO" -> EasyPayProvider.TouchNGo
      "TRUE_MONEY" -> EasyPayProvider.TrueMoney
      "DOKU_WALLET" -> EasyPayProvider.DokuWallet
      "JENIUS_PAY" -> EasyPayProvider.JeniusPay
      "OVO" -> EasyPayProvider.Ovo
      "MAYA" -> EasyPayProvider.Maya
      "QRIS" -> EasyPayProvider.Qris
      "THAI_QR" -> EasyPayProvider.ThaiQr
      else -> EasyPayProvider.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: EasyPayProvider): Unit = encoder.encodeString(value.value)
}

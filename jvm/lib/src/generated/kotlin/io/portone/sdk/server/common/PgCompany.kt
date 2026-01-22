package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** PG사 */
@Serializable(PgCompanySerializer::class)
public sealed interface PgCompany {
  public val value: String
  @Serializable(InicisSerializer::class)
  public data object Inicis : PgCompany {
    override val value: String = "INICIS"
  }
  public object InicisSerializer : KSerializer<Inicis> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Inicis::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Inicis = decoder.decodeString().let {
      if (it != "INICIS") {
        throw SerializationException(it)
      } else {
        return Inicis
      }
    }
    override fun serialize(encoder: Encoder, value: Inicis): Unit = encoder.encodeString(value.value)
  }
  @Serializable(NiceSerializer::class)
  public data object Nice : PgCompany {
    override val value: String = "NICE"
  }
  public object NiceSerializer : KSerializer<Nice> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nice::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nice = decoder.decodeString().let {
      if (it != "NICE") {
        throw SerializationException(it)
      } else {
        return Nice
      }
    }
    override fun serialize(encoder: Encoder, value: Nice): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KcpSerializer::class)
  public data object Kcp : PgCompany {
    override val value: String = "KCP"
  }
  public object KcpSerializer : KSerializer<Kcp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kcp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kcp = decoder.decodeString().let {
      if (it != "KCP") {
        throw SerializationException(it)
      } else {
        return Kcp
      }
    }
    override fun serialize(encoder: Encoder, value: Kcp): Unit = encoder.encodeString(value.value)
  }
  @Serializable(DanalSerializer::class)
  public data object Danal : PgCompany {
    override val value: String = "DANAL"
  }
  public object DanalSerializer : KSerializer<Danal> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Danal::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Danal = decoder.decodeString().let {
      if (it != "DANAL") {
        throw SerializationException(it)
      } else {
        return Danal
      }
    }
    override fun serialize(encoder: Encoder, value: Danal): Unit = encoder.encodeString(value.value)
  }
  @Serializable(TosspaymentsSerializer::class)
  public data object Tosspayments : PgCompany {
    override val value: String = "TOSSPAYMENTS"
  }
  public object TosspaymentsSerializer : KSerializer<Tosspayments> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tosspayments::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tosspayments = decoder.decodeString().let {
      if (it != "TOSSPAYMENTS") {
        throw SerializationException(it)
      } else {
        return Tosspayments
      }
    }
    override fun serialize(encoder: Encoder, value: Tosspayments): Unit = encoder.encodeString(value.value)
  }
  @Serializable(MobiliansSerializer::class)
  public data object Mobilians : PgCompany {
    override val value: String = "MOBILIANS"
  }
  public object MobiliansSerializer : KSerializer<Mobilians> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mobilians::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mobilians = decoder.decodeString().let {
      if (it != "MOBILIANS") {
        throw SerializationException(it)
      } else {
        return Mobilians
      }
    }
    override fun serialize(encoder: Encoder, value: Mobilians): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KiccSerializer::class)
  public data object Kicc : PgCompany {
    override val value: String = "KICC"
  }
  public object KiccSerializer : KSerializer<Kicc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kicc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kicc = decoder.decodeString().let {
      if (it != "KICC") {
        throw SerializationException(it)
      } else {
        return Kicc
      }
    }
    override fun serialize(encoder: Encoder, value: Kicc): Unit = encoder.encodeString(value.value)
  }
  @Serializable(SmartroSerializer::class)
  public data object Smartro : PgCompany {
    override val value: String = "SMARTRO"
  }
  public object SmartroSerializer : KSerializer<Smartro> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Smartro::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Smartro = decoder.decodeString().let {
      if (it != "SMARTRO") {
        throw SerializationException(it)
      } else {
        return Smartro
      }
    }
    override fun serialize(encoder: Encoder, value: Smartro): Unit = encoder.encodeString(value.value)
  }
  @Serializable(DaouSerializer::class)
  public data object Daou : PgCompany {
    override val value: String = "DAOU"
  }
  public object DaouSerializer : KSerializer<Daou> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Daou::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Daou = decoder.decodeString().let {
      if (it != "DAOU") {
        throw SerializationException(it)
      } else {
        return Daou
      }
    }
    override fun serialize(encoder: Encoder, value: Daou): Unit = encoder.encodeString(value.value)
  }
  @Serializable(BluewalnutSerializer::class)
  public data object Bluewalnut : PgCompany {
    override val value: String = "BLUEWALNUT"
  }
  public object BluewalnutSerializer : KSerializer<Bluewalnut> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bluewalnut::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bluewalnut = decoder.decodeString().let {
      if (it != "BLUEWALNUT") {
        throw SerializationException(it)
      } else {
        return Bluewalnut
      }
    }
    override fun serialize(encoder: Encoder, value: Bluewalnut): Unit = encoder.encodeString(value.value)
  }
  @Serializable(PaypalSerializer::class)
  public data object Paypal : PgCompany {
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
  @Serializable(AlipaySerializer::class)
  public data object Alipay : PgCompany {
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
  @Serializable(EximbaySerializer::class)
  public data object Eximbay : PgCompany {
    override val value: String = "EXIMBAY"
  }
  public object EximbaySerializer : KSerializer<Eximbay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Eximbay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Eximbay = decoder.decodeString().let {
      if (it != "EXIMBAY") {
        throw SerializationException(it)
      } else {
        return Eximbay
      }
    }
    override fun serialize(encoder: Encoder, value: Eximbay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(PaymentwallSerializer::class)
  public data object Paymentwall : PgCompany {
    override val value: String = "PAYMENTWALL"
  }
  public object PaymentwallSerializer : KSerializer<Paymentwall> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Paymentwall::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Paymentwall = decoder.decodeString().let {
      if (it != "PAYMENTWALL") {
        throw SerializationException(it)
      } else {
        return Paymentwall
      }
    }
    override fun serialize(encoder: Encoder, value: Paymentwall): Unit = encoder.encodeString(value.value)
  }
  @Serializable(SettleSerializer::class)
  public data object Settle : PgCompany {
    override val value: String = "SETTLE"
  }
  public object SettleSerializer : KSerializer<Settle> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Settle::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Settle = decoder.decodeString().let {
      if (it != "SETTLE") {
        throw SerializationException(it)
      } else {
        return Settle
      }
    }
    override fun serialize(encoder: Encoder, value: Settle): Unit = encoder.encodeString(value.value)
  }
  @Serializable(GalaxiaSerializer::class)
  public data object Galaxia : PgCompany {
    override val value: String = "GALAXIA"
  }
  public object GalaxiaSerializer : KSerializer<Galaxia> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Galaxia::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Galaxia = decoder.decodeString().let {
      if (it != "GALAXIA") {
        throw SerializationException(it)
      } else {
        return Galaxia
      }
    }
    override fun serialize(encoder: Encoder, value: Galaxia): Unit = encoder.encodeString(value.value)
  }
  @Serializable(NaverpaySerializer::class)
  public data object Naverpay : PgCompany {
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
  @Serializable(KakaopaySerializer::class)
  public data object Kakaopay : PgCompany {
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
  @Serializable(SmilepaySerializer::class)
  public data object Smilepay : PgCompany {
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
  @Serializable(KakaoSerializer::class)
  public data object Kakao : PgCompany {
    override val value: String = "KAKAO"
  }
  public object KakaoSerializer : KSerializer<Kakao> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kakao::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kakao = decoder.decodeString().let {
      if (it != "KAKAO") {
        throw SerializationException(it)
      } else {
        return Kakao
      }
    }
    override fun serialize(encoder: Encoder, value: Kakao): Unit = encoder.encodeString(value.value)
  }
  @Serializable(TosspaySerializer::class)
  public data object Tosspay : PgCompany {
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
  @Serializable(ChaiSerializer::class)
  public data object Chai : PgCompany {
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
  @Serializable(PaycoSerializer::class)
  public data object Payco : PgCompany {
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
  @Serializable(PaypleSerializer::class)
  public data object Payple : PgCompany {
    override val value: String = "PAYPLE"
  }
  public object PaypleSerializer : KSerializer<Payple> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Payple::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Payple = decoder.decodeString().let {
      if (it != "PAYPLE") {
        throw SerializationException(it)
      } else {
        return Payple
      }
    }
    override fun serialize(encoder: Encoder, value: Payple): Unit = encoder.encodeString(value.value)
  }
  @Serializable(SyrupSerializer::class)
  public data object Syrup : PgCompany {
    override val value: String = "SYRUP"
  }
  public object SyrupSerializer : KSerializer<Syrup> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Syrup::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Syrup = decoder.decodeString().let {
      if (it != "SYRUP") {
        throw SerializationException(it)
      } else {
        return Syrup
      }
    }
    override fun serialize(encoder: Encoder, value: Syrup): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KsnetSerializer::class)
  public data object Ksnet : PgCompany {
    override val value: String = "KSNET"
  }
  public object KsnetSerializer : KSerializer<Ksnet> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ksnet::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ksnet = decoder.decodeString().let {
      if (it != "KSNET") {
        throw SerializationException(it)
      } else {
        return Ksnet
      }
    }
    override fun serialize(encoder: Encoder, value: Ksnet): Unit = encoder.encodeString(value.value)
  }
  @Serializable(WelcomeSerializer::class)
  public data object Welcome : PgCompany {
    override val value: String = "WELCOME"
  }
  public object WelcomeSerializer : KSerializer<Welcome> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Welcome::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Welcome = decoder.decodeString().let {
      if (it != "WELCOME") {
        throw SerializationException(it)
      } else {
        return Welcome
      }
    }
    override fun serialize(encoder: Encoder, value: Welcome): Unit = encoder.encodeString(value.value)
  }
  @Serializable(JtnetSerializer::class)
  public data object Jtnet : PgCompany {
    override val value: String = "JTNET"
  }
  public object JtnetSerializer : KSerializer<Jtnet> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jtnet::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jtnet = decoder.decodeString().let {
      if (it != "JTNET") {
        throw SerializationException(it)
      } else {
        return Jtnet
      }
    }
    override fun serialize(encoder: Encoder, value: Jtnet): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KpnSerializer::class)
  public data object Kpn : PgCompany {
    override val value: String = "KPN"
  }
  public object KpnSerializer : KSerializer<Kpn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kpn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kpn = decoder.decodeString().let {
      if (it != "KPN") {
        throw SerializationException(it)
      } else {
        return Kpn
      }
    }
    override fun serialize(encoder: Encoder, value: Kpn): Unit = encoder.encodeString(value.value)
  }
  @Serializable(HyphenSerializer::class)
  public data object Hyphen : PgCompany {
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
  @Serializable(PayletterSerializer::class)
  public data object Payletter : PgCompany {
    override val value: String = "PAYLETTER"
  }
  public object PayletterSerializer : KSerializer<Payletter> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Payletter::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Payletter = decoder.decodeString().let {
      if (it != "PAYLETTER") {
        throw SerializationException(it)
      } else {
        return Payletter
      }
    }
    override fun serialize(encoder: Encoder, value: Payletter): Unit = encoder.encodeString(value.value)
  }
  @Serializable(TripleASerializer::class)
  public data object TripleA : PgCompany {
    override val value: String = "TRIPLE_A"
  }
  public object TripleASerializer : KSerializer<TripleA> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TripleA::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TripleA = decoder.decodeString().let {
      if (it != "TRIPLE_A") {
        throw SerializationException(it)
      } else {
        return TripleA
      }
    }
    override fun serialize(encoder: Encoder, value: TripleA): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PgCompany
}


public object PgCompanySerializer : KSerializer<PgCompany> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PgCompany::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PgCompany {
    val value = decoder.decodeString()
    return when (value) {
      "INICIS" -> PgCompany.Inicis
      "NICE" -> PgCompany.Nice
      "KCP" -> PgCompany.Kcp
      "DANAL" -> PgCompany.Danal
      "TOSSPAYMENTS" -> PgCompany.Tosspayments
      "MOBILIANS" -> PgCompany.Mobilians
      "KICC" -> PgCompany.Kicc
      "SMARTRO" -> PgCompany.Smartro
      "DAOU" -> PgCompany.Daou
      "BLUEWALNUT" -> PgCompany.Bluewalnut
      "PAYPAL" -> PgCompany.Paypal
      "ALIPAY" -> PgCompany.Alipay
      "EXIMBAY" -> PgCompany.Eximbay
      "PAYMENTWALL" -> PgCompany.Paymentwall
      "SETTLE" -> PgCompany.Settle
      "GALAXIA" -> PgCompany.Galaxia
      "NAVERPAY" -> PgCompany.Naverpay
      "KAKAOPAY" -> PgCompany.Kakaopay
      "SMILEPAY" -> PgCompany.Smilepay
      "KAKAO" -> PgCompany.Kakao
      "TOSSPAY" -> PgCompany.Tosspay
      "CHAI" -> PgCompany.Chai
      "PAYCO" -> PgCompany.Payco
      "PAYPLE" -> PgCompany.Payple
      "SYRUP" -> PgCompany.Syrup
      "KSNET" -> PgCompany.Ksnet
      "WELCOME" -> PgCompany.Welcome
      "JTNET" -> PgCompany.Jtnet
      "KPN" -> PgCompany.Kpn
      "HYPHEN" -> PgCompany.Hyphen
      "PAYLETTER" -> PgCompany.Payletter
      "TRIPLE_A" -> PgCompany.TripleA
      else -> PgCompany.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PgCompany): Unit = encoder.encodeString(value.value)
}

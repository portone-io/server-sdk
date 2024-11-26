package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** PG사 결제 모듈 */
@Serializable(PgProviderSerializer::class)
public sealed interface PgProvider {
  public val value: String
  @Serializable(Html5InicisSerializer::class)
  public data object Html5Inicis : PgProvider {
    override val value: String = "HTML5_INICIS"
  }
  private object Html5InicisSerializer : KSerializer<Html5Inicis> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Html5Inicis::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Html5Inicis = decoder.decodeString().let {
      if (it != "HTML5_INICIS") {
        throw SerializationException(it)
      } else {
        return Html5Inicis
      }
    }
    override fun serialize(encoder: Encoder, value: Html5Inicis) = encoder.encodeString(value.value)
  }
  @Serializable(PaypalSerializer::class)
  public data object Paypal : PgProvider {
    override val value: String = "PAYPAL"
  }
  private object PaypalSerializer : KSerializer<Paypal> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Paypal::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Paypal = decoder.decodeString().let {
      if (it != "PAYPAL") {
        throw SerializationException(it)
      } else {
        return Paypal
      }
    }
    override fun serialize(encoder: Encoder, value: Paypal) = encoder.encodeString(value.value)
  }
  @Serializable(PaypalV2Serializer::class)
  public data object PaypalV2 : PgProvider {
    override val value: String = "PAYPAL_V2"
  }
  private object PaypalV2Serializer : KSerializer<PaypalV2> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaypalV2::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PaypalV2 = decoder.decodeString().let {
      if (it != "PAYPAL_V2") {
        throw SerializationException(it)
      } else {
        return PaypalV2
      }
    }
    override fun serialize(encoder: Encoder, value: PaypalV2) = encoder.encodeString(value.value)
  }
  @Serializable(InicisSerializer::class)
  public data object Inicis : PgProvider {
    override val value: String = "INICIS"
  }
  private object InicisSerializer : KSerializer<Inicis> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Inicis::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Inicis = decoder.decodeString().let {
      if (it != "INICIS") {
        throw SerializationException(it)
      } else {
        return Inicis
      }
    }
    override fun serialize(encoder: Encoder, value: Inicis) = encoder.encodeString(value.value)
  }
  @Serializable(DanalSerializer::class)
  public data object Danal : PgProvider {
    override val value: String = "DANAL"
  }
  private object DanalSerializer : KSerializer<Danal> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Danal::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Danal = decoder.decodeString().let {
      if (it != "DANAL") {
        throw SerializationException(it)
      } else {
        return Danal
      }
    }
    override fun serialize(encoder: Encoder, value: Danal) = encoder.encodeString(value.value)
  }
  @Serializable(NiceSerializer::class)
  public data object Nice : PgProvider {
    override val value: String = "NICE"
  }
  private object NiceSerializer : KSerializer<Nice> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nice::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nice = decoder.decodeString().let {
      if (it != "NICE") {
        throw SerializationException(it)
      } else {
        return Nice
      }
    }
    override fun serialize(encoder: Encoder, value: Nice) = encoder.encodeString(value.value)
  }
  @Serializable(DanalTpaySerializer::class)
  public data object DanalTpay : PgProvider {
    override val value: String = "DANAL_TPAY"
  }
  private object DanalTpaySerializer : KSerializer<DanalTpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DanalTpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DanalTpay = decoder.decodeString().let {
      if (it != "DANAL_TPAY") {
        throw SerializationException(it)
      } else {
        return DanalTpay
      }
    }
    override fun serialize(encoder: Encoder, value: DanalTpay) = encoder.encodeString(value.value)
  }
  @Serializable(JtnetSerializer::class)
  public data object Jtnet : PgProvider {
    override val value: String = "JTNET"
  }
  private object JtnetSerializer : KSerializer<Jtnet> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jtnet::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jtnet = decoder.decodeString().let {
      if (it != "JTNET") {
        throw SerializationException(it)
      } else {
        return Jtnet
      }
    }
    override fun serialize(encoder: Encoder, value: Jtnet) = encoder.encodeString(value.value)
  }
  @Serializable(UplusSerializer::class)
  public data object Uplus : PgProvider {
    override val value: String = "UPLUS"
  }
  private object UplusSerializer : KSerializer<Uplus> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uplus::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uplus = decoder.decodeString().let {
      if (it != "UPLUS") {
        throw SerializationException(it)
      } else {
        return Uplus
      }
    }
    override fun serialize(encoder: Encoder, value: Uplus) = encoder.encodeString(value.value)
  }
  @Serializable(NaverpaySerializer::class)
  public data object Naverpay : PgProvider {
    override val value: String = "NAVERPAY"
  }
  private object NaverpaySerializer : KSerializer<Naverpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Naverpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Naverpay = decoder.decodeString().let {
      if (it != "NAVERPAY") {
        throw SerializationException(it)
      } else {
        return Naverpay
      }
    }
    override fun serialize(encoder: Encoder, value: Naverpay) = encoder.encodeString(value.value)
  }
  @Serializable(KakaoSerializer::class)
  public data object Kakao : PgProvider {
    override val value: String = "KAKAO"
  }
  private object KakaoSerializer : KSerializer<Kakao> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kakao::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kakao = decoder.decodeString().let {
      if (it != "KAKAO") {
        throw SerializationException(it)
      } else {
        return Kakao
      }
    }
    override fun serialize(encoder: Encoder, value: Kakao) = encoder.encodeString(value.value)
  }
  @Serializable(SettleSerializer::class)
  public data object Settle : PgProvider {
    override val value: String = "SETTLE"
  }
  private object SettleSerializer : KSerializer<Settle> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Settle::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Settle = decoder.decodeString().let {
      if (it != "SETTLE") {
        throw SerializationException(it)
      } else {
        return Settle
      }
    }
    override fun serialize(encoder: Encoder, value: Settle) = encoder.encodeString(value.value)
  }
  @Serializable(KcpSerializer::class)
  public data object Kcp : PgProvider {
    override val value: String = "KCP"
  }
  private object KcpSerializer : KSerializer<Kcp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kcp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kcp = decoder.decodeString().let {
      if (it != "KCP") {
        throw SerializationException(it)
      } else {
        return Kcp
      }
    }
    override fun serialize(encoder: Encoder, value: Kcp) = encoder.encodeString(value.value)
  }
  @Serializable(MobiliansSerializer::class)
  public data object Mobilians : PgProvider {
    override val value: String = "MOBILIANS"
  }
  private object MobiliansSerializer : KSerializer<Mobilians> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mobilians::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mobilians = decoder.decodeString().let {
      if (it != "MOBILIANS") {
        throw SerializationException(it)
      } else {
        return Mobilians
      }
    }
    override fun serialize(encoder: Encoder, value: Mobilians) = encoder.encodeString(value.value)
  }
  @Serializable(KakaopaySerializer::class)
  public data object Kakaopay : PgProvider {
    override val value: String = "KAKAOPAY"
  }
  private object KakaopaySerializer : KSerializer<Kakaopay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kakaopay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kakaopay = decoder.decodeString().let {
      if (it != "KAKAOPAY") {
        throw SerializationException(it)
      } else {
        return Kakaopay
      }
    }
    override fun serialize(encoder: Encoder, value: Kakaopay) = encoder.encodeString(value.value)
  }
  @Serializable(NavercoSerializer::class)
  public data object Naverco : PgProvider {
    override val value: String = "NAVERCO"
  }
  private object NavercoSerializer : KSerializer<Naverco> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Naverco::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Naverco = decoder.decodeString().let {
      if (it != "NAVERCO") {
        throw SerializationException(it)
      } else {
        return Naverco
      }
    }
    override fun serialize(encoder: Encoder, value: Naverco) = encoder.encodeString(value.value)
  }
  @Serializable(SyrupSerializer::class)
  public data object Syrup : PgProvider {
    override val value: String = "SYRUP"
  }
  private object SyrupSerializer : KSerializer<Syrup> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Syrup::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Syrup = decoder.decodeString().let {
      if (it != "SYRUP") {
        throw SerializationException(it)
      } else {
        return Syrup
      }
    }
    override fun serialize(encoder: Encoder, value: Syrup) = encoder.encodeString(value.value)
  }
  @Serializable(KiccSerializer::class)
  public data object Kicc : PgProvider {
    override val value: String = "KICC"
  }
  private object KiccSerializer : KSerializer<Kicc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kicc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kicc = decoder.decodeString().let {
      if (it != "KICC") {
        throw SerializationException(it)
      } else {
        return Kicc
      }
    }
    override fun serialize(encoder: Encoder, value: Kicc) = encoder.encodeString(value.value)
  }
  @Serializable(EximbaySerializer::class)
  public data object Eximbay : PgProvider {
    override val value: String = "EXIMBAY"
  }
  private object EximbaySerializer : KSerializer<Eximbay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Eximbay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Eximbay = decoder.decodeString().let {
      if (it != "EXIMBAY") {
        throw SerializationException(it)
      } else {
        return Eximbay
      }
    }
    override fun serialize(encoder: Encoder, value: Eximbay) = encoder.encodeString(value.value)
  }
  @Serializable(SmilepaySerializer::class)
  public data object Smilepay : PgProvider {
    override val value: String = "SMILEPAY"
  }
  private object SmilepaySerializer : KSerializer<Smilepay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Smilepay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Smilepay = decoder.decodeString().let {
      if (it != "SMILEPAY") {
        throw SerializationException(it)
      } else {
        return Smilepay
      }
    }
    override fun serialize(encoder: Encoder, value: Smilepay) = encoder.encodeString(value.value)
  }
  @Serializable(PaycoSerializer::class)
  public data object Payco : PgProvider {
    override val value: String = "PAYCO"
  }
  private object PaycoSerializer : KSerializer<Payco> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Payco::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Payco = decoder.decodeString().let {
      if (it != "PAYCO") {
        throw SerializationException(it)
      } else {
        return Payco
      }
    }
    override fun serialize(encoder: Encoder, value: Payco) = encoder.encodeString(value.value)
  }
  @Serializable(KcpBillingSerializer::class)
  public data object KcpBilling : PgProvider {
    override val value: String = "KCP_BILLING"
  }
  private object KcpBillingSerializer : KSerializer<KcpBilling> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KcpBilling::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KcpBilling = decoder.decodeString().let {
      if (it != "KCP_BILLING") {
        throw SerializationException(it)
      } else {
        return KcpBilling
      }
    }
    override fun serialize(encoder: Encoder, value: KcpBilling) = encoder.encodeString(value.value)
  }
  @Serializable(AlipaySerializer::class)
  public data object Alipay : PgProvider {
    override val value: String = "ALIPAY"
  }
  private object AlipaySerializer : KSerializer<Alipay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Alipay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Alipay = decoder.decodeString().let {
      if (it != "ALIPAY") {
        throw SerializationException(it)
      } else {
        return Alipay
      }
    }
    override fun serialize(encoder: Encoder, value: Alipay) = encoder.encodeString(value.value)
  }
  @Serializable(PaypleSerializer::class)
  public data object Payple : PgProvider {
    override val value: String = "PAYPLE"
  }
  private object PaypleSerializer : KSerializer<Payple> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Payple::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Payple = decoder.decodeString().let {
      if (it != "PAYPLE") {
        throw SerializationException(it)
      } else {
        return Payple
      }
    }
    override fun serialize(encoder: Encoder, value: Payple) = encoder.encodeString(value.value)
  }
  @Serializable(ChaiSerializer::class)
  public data object Chai : PgProvider {
    override val value: String = "CHAI"
  }
  private object ChaiSerializer : KSerializer<Chai> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Chai::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Chai = decoder.decodeString().let {
      if (it != "CHAI") {
        throw SerializationException(it)
      } else {
        return Chai
      }
    }
    override fun serialize(encoder: Encoder, value: Chai) = encoder.encodeString(value.value)
  }
  @Serializable(BluewalnutSerializer::class)
  public data object Bluewalnut : PgProvider {
    override val value: String = "BLUEWALNUT"
  }
  private object BluewalnutSerializer : KSerializer<Bluewalnut> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bluewalnut::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bluewalnut = decoder.decodeString().let {
      if (it != "BLUEWALNUT") {
        throw SerializationException(it)
      } else {
        return Bluewalnut
      }
    }
    override fun serialize(encoder: Encoder, value: Bluewalnut) = encoder.encodeString(value.value)
  }
  @Serializable(SmartroSerializer::class)
  public data object Smartro : PgProvider {
    override val value: String = "SMARTRO"
  }
  private object SmartroSerializer : KSerializer<Smartro> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Smartro::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Smartro = decoder.decodeString().let {
      if (it != "SMARTRO") {
        throw SerializationException(it)
      } else {
        return Smartro
      }
    }
    override fun serialize(encoder: Encoder, value: Smartro) = encoder.encodeString(value.value)
  }
  @Serializable(SmartroV2Serializer::class)
  public data object SmartroV2 : PgProvider {
    override val value: String = "SMARTRO_V2"
  }
  private object SmartroV2Serializer : KSerializer<SmartroV2> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SmartroV2::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SmartroV2 = decoder.decodeString().let {
      if (it != "SMARTRO_V2") {
        throw SerializationException(it)
      } else {
        return SmartroV2
      }
    }
    override fun serialize(encoder: Encoder, value: SmartroV2) = encoder.encodeString(value.value)
  }
  @Serializable(PaymentwallSerializer::class)
  public data object Paymentwall : PgProvider {
    override val value: String = "PAYMENTWALL"
  }
  private object PaymentwallSerializer : KSerializer<Paymentwall> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Paymentwall::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Paymentwall = decoder.decodeString().let {
      if (it != "PAYMENTWALL") {
        throw SerializationException(it)
      } else {
        return Paymentwall
      }
    }
    override fun serialize(encoder: Encoder, value: Paymentwall) = encoder.encodeString(value.value)
  }
  @Serializable(TosspaymentsSerializer::class)
  public data object Tosspayments : PgProvider {
    override val value: String = "TOSSPAYMENTS"
  }
  private object TosspaymentsSerializer : KSerializer<Tosspayments> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tosspayments::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tosspayments = decoder.decodeString().let {
      if (it != "TOSSPAYMENTS") {
        throw SerializationException(it)
      } else {
        return Tosspayments
      }
    }
    override fun serialize(encoder: Encoder, value: Tosspayments) = encoder.encodeString(value.value)
  }
  @Serializable(KcpQuickSerializer::class)
  public data object KcpQuick : PgProvider {
    override val value: String = "KCP_QUICK"
  }
  private object KcpQuickSerializer : KSerializer<KcpQuick> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KcpQuick::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KcpQuick = decoder.decodeString().let {
      if (it != "KCP_QUICK") {
        throw SerializationException(it)
      } else {
        return KcpQuick
      }
    }
    override fun serialize(encoder: Encoder, value: KcpQuick) = encoder.encodeString(value.value)
  }
  @Serializable(DaouSerializer::class)
  public data object Daou : PgProvider {
    override val value: String = "DAOU"
  }
  private object DaouSerializer : KSerializer<Daou> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Daou::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Daou = decoder.decodeString().let {
      if (it != "DAOU") {
        throw SerializationException(it)
      } else {
        return Daou
      }
    }
    override fun serialize(encoder: Encoder, value: Daou) = encoder.encodeString(value.value)
  }
  @Serializable(GalaxiaSerializer::class)
  public data object Galaxia : PgProvider {
    override val value: String = "GALAXIA"
  }
  private object GalaxiaSerializer : KSerializer<Galaxia> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Galaxia::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Galaxia = decoder.decodeString().let {
      if (it != "GALAXIA") {
        throw SerializationException(it)
      } else {
        return Galaxia
      }
    }
    override fun serialize(encoder: Encoder, value: Galaxia) = encoder.encodeString(value.value)
  }
  @Serializable(TosspaySerializer::class)
  public data object Tosspay : PgProvider {
    override val value: String = "TOSSPAY"
  }
  private object TosspaySerializer : KSerializer<Tosspay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tosspay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tosspay = decoder.decodeString().let {
      if (it != "TOSSPAY") {
        throw SerializationException(it)
      } else {
        return Tosspay
      }
    }
    override fun serialize(encoder: Encoder, value: Tosspay) = encoder.encodeString(value.value)
  }
  @Serializable(KcpDirectSerializer::class)
  public data object KcpDirect : PgProvider {
    override val value: String = "KCP_DIRECT"
  }
  private object KcpDirectSerializer : KSerializer<KcpDirect> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KcpDirect::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KcpDirect = decoder.decodeString().let {
      if (it != "KCP_DIRECT") {
        throw SerializationException(it)
      } else {
        return KcpDirect
      }
    }
    override fun serialize(encoder: Encoder, value: KcpDirect) = encoder.encodeString(value.value)
  }
  @Serializable(SettleAccSerializer::class)
  public data object SettleAcc : PgProvider {
    override val value: String = "SETTLE_ACC"
  }
  private object SettleAccSerializer : KSerializer<SettleAcc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettleAcc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettleAcc = decoder.decodeString().let {
      if (it != "SETTLE_ACC") {
        throw SerializationException(it)
      } else {
        return SettleAcc
      }
    }
    override fun serialize(encoder: Encoder, value: SettleAcc) = encoder.encodeString(value.value)
  }
  @Serializable(SettleFirmSerializer::class)
  public data object SettleFirm : PgProvider {
    override val value: String = "SETTLE_FIRM"
  }
  private object SettleFirmSerializer : KSerializer<SettleFirm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettleFirm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettleFirm = decoder.decodeString().let {
      if (it != "SETTLE_FIRM") {
        throw SerializationException(it)
      } else {
        return SettleFirm
      }
    }
    override fun serialize(encoder: Encoder, value: SettleFirm) = encoder.encodeString(value.value)
  }
  @Serializable(InicisUnifiedSerializer::class)
  public data object InicisUnified : PgProvider {
    override val value: String = "INICIS_UNIFIED"
  }
  private object InicisUnifiedSerializer : KSerializer<InicisUnified> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(InicisUnified::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): InicisUnified = decoder.decodeString().let {
      if (it != "INICIS_UNIFIED") {
        throw SerializationException(it)
      } else {
        return InicisUnified
      }
    }
    override fun serialize(encoder: Encoder, value: InicisUnified) = encoder.encodeString(value.value)
  }
  @Serializable(KsnetSerializer::class)
  public data object Ksnet : PgProvider {
    override val value: String = "KSNET"
  }
  private object KsnetSerializer : KSerializer<Ksnet> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ksnet::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ksnet = decoder.decodeString().let {
      if (it != "KSNET") {
        throw SerializationException(it)
      } else {
        return Ksnet
      }
    }
    override fun serialize(encoder: Encoder, value: Ksnet) = encoder.encodeString(value.value)
  }
  @Serializable(PinpaySerializer::class)
  public data object Pinpay : PgProvider {
    override val value: String = "PINPAY"
  }
  private object PinpaySerializer : KSerializer<Pinpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pinpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pinpay = decoder.decodeString().let {
      if (it != "PINPAY") {
        throw SerializationException(it)
      } else {
        return Pinpay
      }
    }
    override fun serialize(encoder: Encoder, value: Pinpay) = encoder.encodeString(value.value)
  }
  @Serializable(NiceV2Serializer::class)
  public data object NiceV2 : PgProvider {
    override val value: String = "NICE_V2"
  }
  private object NiceV2Serializer : KSerializer<NiceV2> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NiceV2::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NiceV2 = decoder.decodeString().let {
      if (it != "NICE_V2") {
        throw SerializationException(it)
      } else {
        return NiceV2
      }
    }
    override fun serialize(encoder: Encoder, value: NiceV2) = encoder.encodeString(value.value)
  }
  @Serializable(TossBrandpaySerializer::class)
  public data object TossBrandpay : PgProvider {
    override val value: String = "TOSS_BRANDPAY"
  }
  private object TossBrandpaySerializer : KSerializer<TossBrandpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TossBrandpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TossBrandpay = decoder.decodeString().let {
      if (it != "TOSS_BRANDPAY") {
        throw SerializationException(it)
      } else {
        return TossBrandpay
      }
    }
    override fun serialize(encoder: Encoder, value: TossBrandpay) = encoder.encodeString(value.value)
  }
  @Serializable(WelcomeSerializer::class)
  public data object Welcome : PgProvider {
    override val value: String = "WELCOME"
  }
  private object WelcomeSerializer : KSerializer<Welcome> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Welcome::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Welcome = decoder.decodeString().let {
      if (it != "WELCOME") {
        throw SerializationException(it)
      } else {
        return Welcome
      }
    }
    override fun serialize(encoder: Encoder, value: Welcome) = encoder.encodeString(value.value)
  }
  @Serializable(TosspayV2Serializer::class)
  public data object TosspayV2 : PgProvider {
    override val value: String = "TOSSPAY_V2"
  }
  private object TosspayV2Serializer : KSerializer<TosspayV2> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TosspayV2::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TosspayV2 = decoder.decodeString().let {
      if (it != "TOSSPAY_V2") {
        throw SerializationException(it)
      } else {
        return TosspayV2
      }
    }
    override fun serialize(encoder: Encoder, value: TosspayV2) = encoder.encodeString(value.value)
  }
  @Serializable(InicisV2Serializer::class)
  public data object InicisV2 : PgProvider {
    override val value: String = "INICIS_V2"
  }
  private object InicisV2Serializer : KSerializer<InicisV2> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(InicisV2::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): InicisV2 = decoder.decodeString().let {
      if (it != "INICIS_V2") {
        throw SerializationException(it)
      } else {
        return InicisV2
      }
    }
    override fun serialize(encoder: Encoder, value: InicisV2) = encoder.encodeString(value.value)
  }
  @Serializable(KpnSerializer::class)
  public data object Kpn : PgProvider {
    override val value: String = "KPN"
  }
  private object KpnSerializer : KSerializer<Kpn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kpn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kpn = decoder.decodeString().let {
      if (it != "KPN") {
        throw SerializationException(it)
      } else {
        return Kpn
      }
    }
    override fun serialize(encoder: Encoder, value: Kpn) = encoder.encodeString(value.value)
  }
  @Serializable(KcpV2Serializer::class)
  public data object KcpV2 : PgProvider {
    override val value: String = "KCP_V2"
  }
  private object KcpV2Serializer : KSerializer<KcpV2> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KcpV2::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KcpV2 = decoder.decodeString().let {
      if (it != "KCP_V2") {
        throw SerializationException(it)
      } else {
        return KcpV2
      }
    }
    override fun serialize(encoder: Encoder, value: KcpV2) = encoder.encodeString(value.value)
  }
  @Serializable(HyphenSerializer::class)
  public data object Hyphen : PgProvider {
    override val value: String = "HYPHEN"
  }
  private object HyphenSerializer : KSerializer<Hyphen> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hyphen::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hyphen = decoder.decodeString().let {
      if (it != "HYPHEN") {
        throw SerializationException(it)
      } else {
        return Hyphen
      }
    }
    override fun serialize(encoder: Encoder, value: Hyphen) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PgProvider
}


private object PgProviderSerializer : KSerializer<PgProvider> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PgProvider::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PgProvider {
    val value = decoder.decodeString()
    return when (value) {
      "HTML5_INICIS" -> PgProvider.Html5Inicis
      "PAYPAL" -> PgProvider.Paypal
      "PAYPAL_V2" -> PgProvider.PaypalV2
      "INICIS" -> PgProvider.Inicis
      "DANAL" -> PgProvider.Danal
      "NICE" -> PgProvider.Nice
      "DANAL_TPAY" -> PgProvider.DanalTpay
      "JTNET" -> PgProvider.Jtnet
      "UPLUS" -> PgProvider.Uplus
      "NAVERPAY" -> PgProvider.Naverpay
      "KAKAO" -> PgProvider.Kakao
      "SETTLE" -> PgProvider.Settle
      "KCP" -> PgProvider.Kcp
      "MOBILIANS" -> PgProvider.Mobilians
      "KAKAOPAY" -> PgProvider.Kakaopay
      "NAVERCO" -> PgProvider.Naverco
      "SYRUP" -> PgProvider.Syrup
      "KICC" -> PgProvider.Kicc
      "EXIMBAY" -> PgProvider.Eximbay
      "SMILEPAY" -> PgProvider.Smilepay
      "PAYCO" -> PgProvider.Payco
      "KCP_BILLING" -> PgProvider.KcpBilling
      "ALIPAY" -> PgProvider.Alipay
      "PAYPLE" -> PgProvider.Payple
      "CHAI" -> PgProvider.Chai
      "BLUEWALNUT" -> PgProvider.Bluewalnut
      "SMARTRO" -> PgProvider.Smartro
      "SMARTRO_V2" -> PgProvider.SmartroV2
      "PAYMENTWALL" -> PgProvider.Paymentwall
      "TOSSPAYMENTS" -> PgProvider.Tosspayments
      "KCP_QUICK" -> PgProvider.KcpQuick
      "DAOU" -> PgProvider.Daou
      "GALAXIA" -> PgProvider.Galaxia
      "TOSSPAY" -> PgProvider.Tosspay
      "KCP_DIRECT" -> PgProvider.KcpDirect
      "SETTLE_ACC" -> PgProvider.SettleAcc
      "SETTLE_FIRM" -> PgProvider.SettleFirm
      "INICIS_UNIFIED" -> PgProvider.InicisUnified
      "KSNET" -> PgProvider.Ksnet
      "PINPAY" -> PgProvider.Pinpay
      "NICE_V2" -> PgProvider.NiceV2
      "TOSS_BRANDPAY" -> PgProvider.TossBrandpay
      "WELCOME" -> PgProvider.Welcome
      "TOSSPAY_V2" -> PgProvider.TosspayV2
      "INICIS_V2" -> PgProvider.InicisV2
      "KPN" -> PgProvider.Kpn
      "KCP_V2" -> PgProvider.KcpV2
      "HYPHEN" -> PgProvider.Hyphen
      else -> PgProvider.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PgProvider) = encoder.encodeString(value.value)
}

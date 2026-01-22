package io.portone.sdk.server.reconciliation

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(ReconciliationPgProviderSerializer::class)
public sealed interface ReconciliationPgProvider {
  public val value: String
  @Serializable(KakaopaySerializer::class)
  public data object Kakaopay : ReconciliationPgProvider {
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
  @Serializable(NicepaySerializer::class)
  public data object Nicepay : ReconciliationPgProvider {
    override val value: String = "NICEPAY"
  }
  public object NicepaySerializer : KSerializer<Nicepay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nicepay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nicepay = decoder.decodeString().let {
      if (it != "NICEPAY") {
        throw SerializationException(it)
      } else {
        return Nicepay
      }
    }
    override fun serialize(encoder: Encoder, value: Nicepay): Unit = encoder.encodeString(value.value)
  }
  @Serializable(NaverpaySerializer::class)
  public data object Naverpay : ReconciliationPgProvider {
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
  @Serializable(UplusSerializer::class)
  public data object Uplus : ReconciliationPgProvider {
    override val value: String = "UPLUS"
  }
  public object UplusSerializer : KSerializer<Uplus> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uplus::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uplus = decoder.decodeString().let {
      if (it != "UPLUS") {
        throw SerializationException(it)
      } else {
        return Uplus
      }
    }
    override fun serialize(encoder: Encoder, value: Uplus): Unit = encoder.encodeString(value.value)
  }
  @Serializable(TosspaymentsSerializer::class)
  public data object Tosspayments : ReconciliationPgProvider {
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
  @Serializable(TosspaySerializer::class)
  public data object Tosspay : ReconciliationPgProvider {
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
  @Serializable(PaycoSerializer::class)
  public data object Payco : ReconciliationPgProvider {
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
  @Serializable(KcpSerializer::class)
  public data object Kcp : ReconciliationPgProvider {
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
  public data object Danal : ReconciliationPgProvider {
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
  @Serializable(EximbaySerializer::class)
  public data object Eximbay : ReconciliationPgProvider {
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
  @Serializable(InicisSerializer::class)
  public data object Inicis : ReconciliationPgProvider {
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
  @Serializable(HectoSerializer::class)
  public data object Hecto : ReconciliationPgProvider {
    override val value: String = "HECTO"
  }
  public object HectoSerializer : KSerializer<Hecto> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hecto::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hecto = decoder.decodeString().let {
      if (it != "HECTO") {
        throw SerializationException(it)
      } else {
        return Hecto
      }
    }
    override fun serialize(encoder: Encoder, value: Hecto): Unit = encoder.encodeString(value.value)
  }
  @Serializable(KsnetSerializer::class)
  public data object Ksnet : ReconciliationPgProvider {
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
  @Serializable(KpnSerializer::class)
  public data object Kpn : ReconciliationPgProvider {
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
  public data object Hyphen : ReconciliationPgProvider {
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
  @Serializable(PaypalSerializer::class)
  public data object Paypal : ReconciliationPgProvider {
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
  @Serializable(HectoEasySerializer::class)
  public data object HectoEasy : ReconciliationPgProvider {
    override val value: String = "HECTO_EASY"
  }
  public object HectoEasySerializer : KSerializer<HectoEasy> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HectoEasy::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HectoEasy = decoder.decodeString().let {
      if (it != "HECTO_EASY") {
        throw SerializationException(it)
      } else {
        return HectoEasy
      }
    }
    override fun serialize(encoder: Encoder, value: HectoEasy): Unit = encoder.encodeString(value.value)
  }
  @Serializable(MobiliansSerializer::class)
  public data object Mobilians : ReconciliationPgProvider {
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
  @Serializable(PayletterGlobalSerializer::class)
  public data object PayletterGlobal : ReconciliationPgProvider {
    override val value: String = "PAYLETTER_GLOBAL"
  }
  public object PayletterGlobalSerializer : KSerializer<PayletterGlobal> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PayletterGlobal::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PayletterGlobal = decoder.decodeString().let {
      if (it != "PAYLETTER_GLOBAL") {
        throw SerializationException(it)
      } else {
        return PayletterGlobal
      }
    }
    override fun serialize(encoder: Encoder, value: PayletterGlobal): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : ReconciliationPgProvider
}


public object ReconciliationPgProviderSerializer : KSerializer<ReconciliationPgProvider> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ReconciliationPgProvider::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): ReconciliationPgProvider {
    val value = decoder.decodeString()
    return when (value) {
      "KAKAOPAY" -> ReconciliationPgProvider.Kakaopay
      "NICEPAY" -> ReconciliationPgProvider.Nicepay
      "NAVERPAY" -> ReconciliationPgProvider.Naverpay
      "UPLUS" -> ReconciliationPgProvider.Uplus
      "TOSSPAYMENTS" -> ReconciliationPgProvider.Tosspayments
      "TOSSPAY" -> ReconciliationPgProvider.Tosspay
      "PAYCO" -> ReconciliationPgProvider.Payco
      "KCP" -> ReconciliationPgProvider.Kcp
      "DANAL" -> ReconciliationPgProvider.Danal
      "EXIMBAY" -> ReconciliationPgProvider.Eximbay
      "INICIS" -> ReconciliationPgProvider.Inicis
      "HECTO" -> ReconciliationPgProvider.Hecto
      "KSNET" -> ReconciliationPgProvider.Ksnet
      "KPN" -> ReconciliationPgProvider.Kpn
      "HYPHEN" -> ReconciliationPgProvider.Hyphen
      "PAYPAL" -> ReconciliationPgProvider.Paypal
      "HECTO_EASY" -> ReconciliationPgProvider.HectoEasy
      "MOBILIANS" -> ReconciliationPgProvider.Mobilians
      "PAYLETTER_GLOBAL" -> ReconciliationPgProvider.PayletterGlobal
      else -> ReconciliationPgProvider.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: ReconciliationPgProvider): Unit = encoder.encodeString(value.value)
}

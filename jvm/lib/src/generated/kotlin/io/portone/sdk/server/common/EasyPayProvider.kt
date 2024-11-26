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
  private object SamsungpaySerializer : KSerializer<Samsungpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Samsungpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Samsungpay = decoder.decodeString().let {
      if (it != "SAMSUNGPAY") {
        throw SerializationException(it)
      } else {
        return Samsungpay
      }
    }
    override fun serialize(encoder: Encoder, value: Samsungpay) = encoder.encodeString(value.value)
  }
  @Serializable(KakaopaySerializer::class)
  public data object Kakaopay : EasyPayProvider {
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
  @Serializable(NaverpaySerializer::class)
  public data object Naverpay : EasyPayProvider {
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
  @Serializable(PaycoSerializer::class)
  public data object Payco : EasyPayProvider {
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
  @Serializable(SsgpaySerializer::class)
  public data object Ssgpay : EasyPayProvider {
    override val value: String = "SSGPAY"
  }
  private object SsgpaySerializer : KSerializer<Ssgpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ssgpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ssgpay = decoder.decodeString().let {
      if (it != "SSGPAY") {
        throw SerializationException(it)
      } else {
        return Ssgpay
      }
    }
    override fun serialize(encoder: Encoder, value: Ssgpay) = encoder.encodeString(value.value)
  }
  @Serializable(ChaiSerializer::class)
  public data object Chai : EasyPayProvider {
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
  @Serializable(LpaySerializer::class)
  public data object Lpay : EasyPayProvider {
    override val value: String = "LPAY"
  }
  private object LpaySerializer : KSerializer<Lpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lpay = decoder.decodeString().let {
      if (it != "LPAY") {
        throw SerializationException(it)
      } else {
        return Lpay
      }
    }
    override fun serialize(encoder: Encoder, value: Lpay) = encoder.encodeString(value.value)
  }
  @Serializable(KpaySerializer::class)
  public data object Kpay : EasyPayProvider {
    override val value: String = "KPAY"
  }
  private object KpaySerializer : KSerializer<Kpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kpay = decoder.decodeString().let {
      if (it != "KPAY") {
        throw SerializationException(it)
      } else {
        return Kpay
      }
    }
    override fun serialize(encoder: Encoder, value: Kpay) = encoder.encodeString(value.value)
  }
  @Serializable(TosspaySerializer::class)
  public data object Tosspay : EasyPayProvider {
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
  @Serializable(LgpaySerializer::class)
  public data object Lgpay : EasyPayProvider {
    override val value: String = "LGPAY"
  }
  private object LgpaySerializer : KSerializer<Lgpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lgpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lgpay = decoder.decodeString().let {
      if (it != "LGPAY") {
        throw SerializationException(it)
      } else {
        return Lgpay
      }
    }
    override fun serialize(encoder: Encoder, value: Lgpay) = encoder.encodeString(value.value)
  }
  @Serializable(PinpaySerializer::class)
  public data object Pinpay : EasyPayProvider {
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
  @Serializable(ApplepaySerializer::class)
  public data object Applepay : EasyPayProvider {
    override val value: String = "APPLEPAY"
  }
  private object ApplepaySerializer : KSerializer<Applepay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Applepay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Applepay = decoder.decodeString().let {
      if (it != "APPLEPAY") {
        throw SerializationException(it)
      } else {
        return Applepay
      }
    }
    override fun serialize(encoder: Encoder, value: Applepay) = encoder.encodeString(value.value)
  }
  @Serializable(SkpaySerializer::class)
  public data object Skpay : EasyPayProvider {
    override val value: String = "SKPAY"
  }
  private object SkpaySerializer : KSerializer<Skpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Skpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Skpay = decoder.decodeString().let {
      if (it != "SKPAY") {
        throw SerializationException(it)
      } else {
        return Skpay
      }
    }
    override fun serialize(encoder: Encoder, value: Skpay) = encoder.encodeString(value.value)
  }
  @Serializable(TossBrandpaySerializer::class)
  public data object TossBrandpay : EasyPayProvider {
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
  @Serializable(KbAppSerializer::class)
  public data object KbApp : EasyPayProvider {
    override val value: String = "KB_APP"
  }
  private object KbAppSerializer : KSerializer<KbApp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KbApp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KbApp = decoder.decodeString().let {
      if (it != "KB_APP") {
        throw SerializationException(it)
      } else {
        return KbApp
      }
    }
    override fun serialize(encoder: Encoder, value: KbApp) = encoder.encodeString(value.value)
  }
  @Serializable(AlipaySerializer::class)
  public data object Alipay : EasyPayProvider {
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
  @Serializable(HyphenSerializer::class)
  public data object Hyphen : EasyPayProvider {
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
  @Serializable(TmoneySerializer::class)
  public data object Tmoney : EasyPayProvider {
    override val value: String = "TMONEY"
  }
  private object TmoneySerializer : KSerializer<Tmoney> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tmoney::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tmoney = decoder.decodeString().let {
      if (it != "TMONEY") {
        throw SerializationException(it)
      } else {
        return Tmoney
      }
    }
    override fun serialize(encoder: Encoder, value: Tmoney) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : EasyPayProvider
}


private object EasyPayProviderSerializer : KSerializer<EasyPayProvider> {
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
      else -> EasyPayProvider.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: EasyPayProvider) = encoder.encodeString(value.value)
}

package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제 언어 */
@Serializable(LocaleSerializer::class)
public sealed interface Locale {
  public val value: String
  /** 한국어 (대한민국) */
  @Serializable(KoKrSerializer::class)
  public data object KoKr : Locale {
    override val value: String = "KO_KR"
  }
  private object KoKrSerializer : KSerializer<KoKr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KoKr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KoKr = decoder.decodeString().let {
      if (it != "KO_KR") {
        throw SerializationException(it)
      } else {
        return KoKr
      }
    }
    override fun serialize(encoder: Encoder, value: KoKr) = encoder.encodeString(value.value)
  }
  /** 영어 (미국) */
  @Serializable(EnUsSerializer::class)
  public data object EnUs : Locale {
    override val value: String = "EN_US"
  }
  private object EnUsSerializer : KSerializer<EnUs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(EnUs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): EnUs = decoder.decodeString().let {
      if (it != "EN_US") {
        throw SerializationException(it)
      } else {
        return EnUs
      }
    }
    override fun serialize(encoder: Encoder, value: EnUs) = encoder.encodeString(value.value)
  }
  /** 중국어 (중국) */
  @Serializable(ZhCnSerializer::class)
  public data object ZhCn : Locale {
    override val value: String = "ZH_CN"
  }
  private object ZhCnSerializer : KSerializer<ZhCn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ZhCn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ZhCn = decoder.decodeString().let {
      if (it != "ZH_CN") {
        throw SerializationException(it)
      } else {
        return ZhCn
      }
    }
    override fun serialize(encoder: Encoder, value: ZhCn) = encoder.encodeString(value.value)
  }
  /** 중국어 (대만) */
  @Serializable(ZhTwSerializer::class)
  public data object ZhTw : Locale {
    override val value: String = "ZH_TW"
  }
  private object ZhTwSerializer : KSerializer<ZhTw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ZhTw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ZhTw = decoder.decodeString().let {
      if (it != "ZH_TW") {
        throw SerializationException(it)
      } else {
        return ZhTw
      }
    }
    override fun serialize(encoder: Encoder, value: ZhTw) = encoder.encodeString(value.value)
  }
  /** 일본어 (일본) */
  @Serializable(JaJpSerializer::class)
  public data object JaJp : Locale {
    override val value: String = "JA_JP"
  }
  private object JaJpSerializer : KSerializer<JaJp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(JaJp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): JaJp = decoder.decodeString().let {
      if (it != "JA_JP") {
        throw SerializationException(it)
      } else {
        return JaJp
      }
    }
    override fun serialize(encoder: Encoder, value: JaJp) = encoder.encodeString(value.value)
  }
  /** 러시아어 (러시아) */
  @Serializable(RuRuSerializer::class)
  public data object RuRu : Locale {
    override val value: String = "RU_RU"
  }
  private object RuRuSerializer : KSerializer<RuRu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(RuRu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): RuRu = decoder.decodeString().let {
      if (it != "RU_RU") {
        throw SerializationException(it)
      } else {
        return RuRu
      }
    }
    override fun serialize(encoder: Encoder, value: RuRu) = encoder.encodeString(value.value)
  }
  /** 타이어 (타이) */
  @Serializable(ThThSerializer::class)
  public data object ThTh : Locale {
    override val value: String = "TH_TH"
  }
  private object ThThSerializer : KSerializer<ThTh> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ThTh::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ThTh = decoder.decodeString().let {
      if (it != "TH_TH") {
        throw SerializationException(it)
      } else {
        return ThTh
      }
    }
    override fun serialize(encoder: Encoder, value: ThTh) = encoder.encodeString(value.value)
  }
  /** 베트남어 (베트남) */
  @Serializable(ViVnSerializer::class)
  public data object ViVn : Locale {
    override val value: String = "VI_VN"
  }
  private object ViVnSerializer : KSerializer<ViVn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ViVn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ViVn = decoder.decodeString().let {
      if (it != "VI_VN") {
        throw SerializationException(it)
      } else {
        return ViVn
      }
    }
    override fun serialize(encoder: Encoder, value: ViVn) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Locale
}


private object LocaleSerializer : KSerializer<Locale> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Locale::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): Locale {
    val value = decoder.decodeString()
    return when (value) {
      "KO_KR" -> Locale.KoKr
      "EN_US" -> Locale.EnUs
      "ZH_CN" -> Locale.ZhCn
      "ZH_TW" -> Locale.ZhTw
      "JA_JP" -> Locale.JaJp
      "RU_RU" -> Locale.RuRu
      "TH_TH" -> Locale.ThTh
      "VI_VN" -> Locale.ViVn
      else -> Locale.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: Locale) = encoder.encodeString(value.value)
}

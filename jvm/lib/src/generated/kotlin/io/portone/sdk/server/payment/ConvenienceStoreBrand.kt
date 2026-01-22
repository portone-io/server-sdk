package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 편의점 브랜드 */
@Serializable(ConvenienceStoreBrandSerializer::class)
public sealed interface ConvenienceStoreBrand {
  public val value: String
  /** 로손 */
  @Serializable(LawsonSerializer::class)
  public data object Lawson : ConvenienceStoreBrand {
    override val value: String = "LAWSON"
  }
  public object LawsonSerializer : KSerializer<Lawson> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lawson::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lawson = decoder.decodeString().let {
      if (it != "LAWSON") {
        throw SerializationException(it)
      } else {
        return Lawson
      }
    }
    override fun serialize(encoder: Encoder, value: Lawson): Unit = encoder.encodeString(value.value)
  }
  /** 패밀리마트 */
  @Serializable(FamilyMartSerializer::class)
  public data object FamilyMart : ConvenienceStoreBrand {
    override val value: String = "FAMILY_MART"
  }
  public object FamilyMartSerializer : KSerializer<FamilyMart> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(FamilyMart::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): FamilyMart = decoder.decodeString().let {
      if (it != "FAMILY_MART") {
        throw SerializationException(it)
      } else {
        return FamilyMart
      }
    }
    override fun serialize(encoder: Encoder, value: FamilyMart): Unit = encoder.encodeString(value.value)
  }
  /** 미니스톱 */
  @Serializable(MiniStopSerializer::class)
  public data object MiniStop : ConvenienceStoreBrand {
    override val value: String = "MINI_STOP"
  }
  public object MiniStopSerializer : KSerializer<MiniStop> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(MiniStop::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): MiniStop = decoder.decodeString().let {
      if (it != "MINI_STOP") {
        throw SerializationException(it)
      } else {
        return MiniStop
      }
    }
    override fun serialize(encoder: Encoder, value: MiniStop): Unit = encoder.encodeString(value.value)
  }
  /** 세븐일레븐 */
  @Serializable(SevenElevenSerializer::class)
  public data object SevenEleven : ConvenienceStoreBrand {
    override val value: String = "SEVEN_ELEVEN"
  }
  public object SevenElevenSerializer : KSerializer<SevenEleven> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SevenEleven::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SevenEleven = decoder.decodeString().let {
      if (it != "SEVEN_ELEVEN") {
        throw SerializationException(it)
      } else {
        return SevenEleven
      }
    }
    override fun serialize(encoder: Encoder, value: SevenEleven): Unit = encoder.encodeString(value.value)
  }
  /** 세이코마트 */
  @Serializable(SeicomartSerializer::class)
  public data object Seicomart : ConvenienceStoreBrand {
    override val value: String = "SEICOMART"
  }
  public object SeicomartSerializer : KSerializer<Seicomart> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Seicomart::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Seicomart = decoder.decodeString().let {
      if (it != "SEICOMART") {
        throw SerializationException(it)
      } else {
        return Seicomart
      }
    }
    override fun serialize(encoder: Encoder, value: Seicomart): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : ConvenienceStoreBrand
}


public object ConvenienceStoreBrandSerializer : KSerializer<ConvenienceStoreBrand> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ConvenienceStoreBrand::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): ConvenienceStoreBrand {
    val value = decoder.decodeString()
    return when (value) {
      "LAWSON" -> ConvenienceStoreBrand.Lawson
      "FAMILY_MART" -> ConvenienceStoreBrand.FamilyMart
      "MINI_STOP" -> ConvenienceStoreBrand.MiniStop
      "SEVEN_ELEVEN" -> ConvenienceStoreBrand.SevenEleven
      "SEICOMART" -> ConvenienceStoreBrand.Seicomart
      else -> ConvenienceStoreBrand.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: ConvenienceStoreBrand): Unit = encoder.encodeString(value.value)
}

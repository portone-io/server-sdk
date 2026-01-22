package io.portone.sdk.server.identityverification

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 통신사 */
@Serializable(CarrierSerializer::class)
public sealed interface Carrier {
  public val value: String
  /** SKT */
  @Serializable(SktSerializer::class)
  public data object Skt : Carrier {
    override val value: String = "SKT"
  }
  public object SktSerializer : KSerializer<Skt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Skt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Skt = decoder.decodeString().let {
      if (it != "SKT") {
        throw SerializationException(it)
      } else {
        return Skt
      }
    }
    override fun serialize(encoder: Encoder, value: Skt): Unit = encoder.encodeString(value.value)
  }
  /** KT */
  @Serializable(KtSerializer::class)
  public data object Kt : Carrier {
    override val value: String = "KT"
  }
  public object KtSerializer : KSerializer<Kt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kt = decoder.decodeString().let {
      if (it != "KT") {
        throw SerializationException(it)
      } else {
        return Kt
      }
    }
    override fun serialize(encoder: Encoder, value: Kt): Unit = encoder.encodeString(value.value)
  }
  /** LG 유플러스 */
  @Serializable(LguSerializer::class)
  public data object Lgu : Carrier {
    override val value: String = "LGU"
  }
  public object LguSerializer : KSerializer<Lgu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lgu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lgu = decoder.decodeString().let {
      if (it != "LGU") {
        throw SerializationException(it)
      } else {
        return Lgu
      }
    }
    override fun serialize(encoder: Encoder, value: Lgu): Unit = encoder.encodeString(value.value)
  }
  /** SKT 알뜰폰 */
  @Serializable(SktMvnoSerializer::class)
  public data object SktMvno : Carrier {
    override val value: String = "SKT_MVNO"
  }
  public object SktMvnoSerializer : KSerializer<SktMvno> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SktMvno::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SktMvno = decoder.decodeString().let {
      if (it != "SKT_MVNO") {
        throw SerializationException(it)
      } else {
        return SktMvno
      }
    }
    override fun serialize(encoder: Encoder, value: SktMvno): Unit = encoder.encodeString(value.value)
  }
  /** KT 알뜰폰 */
  @Serializable(KtMvnoSerializer::class)
  public data object KtMvno : Carrier {
    override val value: String = "KT_MVNO"
  }
  public object KtMvnoSerializer : KSerializer<KtMvno> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KtMvno::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KtMvno = decoder.decodeString().let {
      if (it != "KT_MVNO") {
        throw SerializationException(it)
      } else {
        return KtMvno
      }
    }
    override fun serialize(encoder: Encoder, value: KtMvno): Unit = encoder.encodeString(value.value)
  }
  /** LGU 알뜰폰 */
  @Serializable(LguMvnoSerializer::class)
  public data object LguMvno : Carrier {
    override val value: String = "LGU_MVNO"
  }
  public object LguMvnoSerializer : KSerializer<LguMvno> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(LguMvno::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): LguMvno = decoder.decodeString().let {
      if (it != "LGU_MVNO") {
        throw SerializationException(it)
      } else {
        return LguMvno
      }
    }
    override fun serialize(encoder: Encoder, value: LguMvno): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Carrier
}


public object CarrierSerializer : KSerializer<Carrier> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Carrier::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): Carrier {
    val value = decoder.decodeString()
    return when (value) {
      "SKT" -> Carrier.Skt
      "KT" -> Carrier.Kt
      "LGU" -> Carrier.Lgu
      "SKT_MVNO" -> Carrier.SktMvno
      "KT_MVNO" -> Carrier.KtMvno
      "LGU_MVNO" -> Carrier.LguMvno
      else -> Carrier.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: Carrier): Unit = encoder.encodeString(value.value)
}

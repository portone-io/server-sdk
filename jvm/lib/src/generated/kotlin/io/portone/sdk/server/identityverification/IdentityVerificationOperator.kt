package io.portone.sdk.server.identityverification

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 본인인증 통신사 */
@Serializable(IdentityVerificationOperatorSerializer::class)
public sealed interface IdentityVerificationOperator {
  public val value: String
  /** SKT */
  @Serializable(SktSerializer::class)
  public data object Skt : IdentityVerificationOperator {
    override val value: String = "SKT"
  }
  private object SktSerializer : KSerializer<Skt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Skt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Skt = decoder.decodeString().let {
      if (it != "SKT") {
        throw SerializationException(it)
      } else {
        return Skt
      }
    }
    override fun serialize(encoder: Encoder, value: Skt) = encoder.encodeString(value.value)
  }
  /** KT */
  @Serializable(KtSerializer::class)
  public data object Kt : IdentityVerificationOperator {
    override val value: String = "KT"
  }
  private object KtSerializer : KSerializer<Kt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kt = decoder.decodeString().let {
      if (it != "KT") {
        throw SerializationException(it)
      } else {
        return Kt
      }
    }
    override fun serialize(encoder: Encoder, value: Kt) = encoder.encodeString(value.value)
  }
  /** LGU */
  @Serializable(LguSerializer::class)
  public data object Lgu : IdentityVerificationOperator {
    override val value: String = "LGU"
  }
  private object LguSerializer : KSerializer<Lgu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lgu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lgu = decoder.decodeString().let {
      if (it != "LGU") {
        throw SerializationException(it)
      } else {
        return Lgu
      }
    }
    override fun serialize(encoder: Encoder, value: Lgu) = encoder.encodeString(value.value)
  }
  /** SKT 알뜰폰 */
  @Serializable(SktMvnoSerializer::class)
  public data object SktMvno : IdentityVerificationOperator {
    override val value: String = "SKT_MVNO"
  }
  private object SktMvnoSerializer : KSerializer<SktMvno> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SktMvno::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SktMvno = decoder.decodeString().let {
      if (it != "SKT_MVNO") {
        throw SerializationException(it)
      } else {
        return SktMvno
      }
    }
    override fun serialize(encoder: Encoder, value: SktMvno) = encoder.encodeString(value.value)
  }
  /** KT 알뜰폰 */
  @Serializable(KtMvnoSerializer::class)
  public data object KtMvno : IdentityVerificationOperator {
    override val value: String = "KT_MVNO"
  }
  private object KtMvnoSerializer : KSerializer<KtMvno> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KtMvno::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KtMvno = decoder.decodeString().let {
      if (it != "KT_MVNO") {
        throw SerializationException(it)
      } else {
        return KtMvno
      }
    }
    override fun serialize(encoder: Encoder, value: KtMvno) = encoder.encodeString(value.value)
  }
  /** LGU 알뜰폰 */
  @Serializable(LguMvnoSerializer::class)
  public data object LguMvno : IdentityVerificationOperator {
    override val value: String = "LGU_MVNO"
  }
  private object LguMvnoSerializer : KSerializer<LguMvno> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(LguMvno::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): LguMvno = decoder.decodeString().let {
      if (it != "LGU_MVNO") {
        throw SerializationException(it)
      } else {
        return LguMvno
      }
    }
    override fun serialize(encoder: Encoder, value: LguMvno) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : IdentityVerificationOperator
}


private object IdentityVerificationOperatorSerializer : KSerializer<IdentityVerificationOperator> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IdentityVerificationOperator::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): IdentityVerificationOperator {
    val value = decoder.decodeString()
    return when (value) {
      "SKT" -> IdentityVerificationOperator.Skt
      "KT" -> IdentityVerificationOperator.Kt
      "LGU" -> IdentityVerificationOperator.Lgu
      "SKT_MVNO" -> IdentityVerificationOperator.SktMvno
      "KT_MVNO" -> IdentityVerificationOperator.KtMvno
      "LGU_MVNO" -> IdentityVerificationOperator.LguMvno
      else -> IdentityVerificationOperator.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: IdentityVerificationOperator) = encoder.encodeString(value.value)
}

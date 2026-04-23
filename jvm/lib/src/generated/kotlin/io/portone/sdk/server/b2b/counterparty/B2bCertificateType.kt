package io.portone.sdk.server.b2b.counterparty

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 인증서 타입 */
@Serializable(B2bCertificateTypeSerializer::class)
public sealed interface B2bCertificateType {
  public val value: String
  /** 전자세금용 공동인증서 */
  @Serializable(ETaxSerializer::class)
  public data object ETax : B2bCertificateType {
    override val value: String = "E_TAX"
  }
  public object ETaxSerializer : KSerializer<ETax> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ETax::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ETax = decoder.decodeString().let {
      if (it != "E_TAX") {
        throw SerializationException(it)
      } else {
        return ETax
      }
    }
    override fun serialize(encoder: Encoder, value: ETax): Unit = encoder.encodeString(value.value)
  }
  /** 특수목적용 공동인증서 */
  @Serializable(PortoneSerializer::class)
  public data object Portone : B2bCertificateType {
    override val value: String = "PORTONE"
  }
  public object PortoneSerializer : KSerializer<Portone> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Portone::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Portone = decoder.decodeString().let {
      if (it != "PORTONE") {
        throw SerializationException(it)
      } else {
        return Portone
      }
    }
    override fun serialize(encoder: Encoder, value: Portone): Unit = encoder.encodeString(value.value)
  }
  /** 기타 */
  @Serializable(EtcSerializer::class)
  public data object Etc : B2bCertificateType {
    override val value: String = "ETC"
  }
  public object EtcSerializer : KSerializer<Etc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Etc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Etc = decoder.decodeString().let {
      if (it != "ETC") {
        throw SerializationException(it)
      } else {
        return Etc
      }
    }
    override fun serialize(encoder: Encoder, value: Etc): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bCertificateType
}


public object B2bCertificateTypeSerializer : KSerializer<B2bCertificateType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bCertificateType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bCertificateType {
    val value = decoder.decodeString()
    return when (value) {
      "E_TAX" -> B2bCertificateType.ETax
      "PORTONE" -> B2bCertificateType.Portone
      "ETC" -> B2bCertificateType.Etc
      else -> B2bCertificateType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bCertificateType): Unit = encoder.encodeString(value.value)
}

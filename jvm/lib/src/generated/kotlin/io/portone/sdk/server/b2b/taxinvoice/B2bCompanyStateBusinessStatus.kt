package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 영업 상태 */
@Serializable(B2bCompanyStateBusinessStatusSerializer::class)
public sealed interface B2bCompanyStateBusinessStatus {
  public val value: String
  /** 영업중 */
  @Serializable(InBusinessSerializer::class)
  public data object InBusiness : B2bCompanyStateBusinessStatus {
    override val value: String = "IN_BUSINESS"
  }
  public object InBusinessSerializer : KSerializer<InBusiness> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(InBusiness::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): InBusiness = decoder.decodeString().let {
      if (it != "IN_BUSINESS") {
        throw SerializationException(it)
      } else {
        return InBusiness
      }
    }
    override fun serialize(encoder: Encoder, value: InBusiness): Unit = encoder.encodeString(value.value)
  }
  /** 폐업 */
  @Serializable(ClosedSerializer::class)
  public data object Closed : B2bCompanyStateBusinessStatus {
    override val value: String = "CLOSED"
  }
  public object ClosedSerializer : KSerializer<Closed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Closed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Closed = decoder.decodeString().let {
      if (it != "CLOSED") {
        throw SerializationException(it)
      } else {
        return Closed
      }
    }
    override fun serialize(encoder: Encoder, value: Closed): Unit = encoder.encodeString(value.value)
  }
  /** 휴업 */
  @Serializable(SuspendedSerializer::class)
  public data object Suspended : B2bCompanyStateBusinessStatus {
    override val value: String = "SUSPENDED"
  }
  public object SuspendedSerializer : KSerializer<Suspended> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Suspended::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Suspended = decoder.decodeString().let {
      if (it != "SUSPENDED") {
        throw SerializationException(it)
      } else {
        return Suspended
      }
    }
    override fun serialize(encoder: Encoder, value: Suspended): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bCompanyStateBusinessStatus
}


public object B2bCompanyStateBusinessStatusSerializer : KSerializer<B2bCompanyStateBusinessStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bCompanyStateBusinessStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bCompanyStateBusinessStatus {
    val value = decoder.decodeString()
    return when (value) {
      "IN_BUSINESS" -> B2bCompanyStateBusinessStatus.InBusiness
      "CLOSED" -> B2bCompanyStateBusinessStatus.Closed
      "SUSPENDED" -> B2bCompanyStateBusinessStatus.Suspended
      else -> B2bCompanyStateBusinessStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bCompanyStateBusinessStatus): Unit = encoder.encodeString(value.value)
}

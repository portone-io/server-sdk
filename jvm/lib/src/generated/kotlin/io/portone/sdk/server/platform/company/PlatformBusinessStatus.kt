package io.portone.sdk.server.platform.company

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 사업자 상태 */
@Serializable(PlatformBusinessStatusSerializer::class)
public sealed interface PlatformBusinessStatus {
  public val value: String
  /** 사업 중 */
  @Serializable(InBusinessSerializer::class)
  public data object InBusiness : PlatformBusinessStatus {
    override val value: String = "IN_BUSINESS"
  }
  private object InBusinessSerializer : KSerializer<InBusiness> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(InBusiness::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): InBusiness = decoder.decodeString().let {
      if (it != "IN_BUSINESS") {
        throw SerializationException(it)
      } else {
        return InBusiness
      }
    }
    override fun serialize(encoder: Encoder, value: InBusiness) = encoder.encodeString(value.value)
  }
  /** 폐업 */
  @Serializable(ClosedSerializer::class)
  public data object Closed : PlatformBusinessStatus {
    override val value: String = "CLOSED"
  }
  private object ClosedSerializer : KSerializer<Closed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Closed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Closed = decoder.decodeString().let {
      if (it != "CLOSED") {
        throw SerializationException(it)
      } else {
        return Closed
      }
    }
    override fun serialize(encoder: Encoder, value: Closed) = encoder.encodeString(value.value)
  }
  /** 휴업 */
  @Serializable(SuspendedSerializer::class)
  public data object Suspended : PlatformBusinessStatus {
    override val value: String = "SUSPENDED"
  }
  private object SuspendedSerializer : KSerializer<Suspended> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Suspended::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Suspended = decoder.decodeString().let {
      if (it != "SUSPENDED") {
        throw SerializationException(it)
      } else {
        return Suspended
      }
    }
    override fun serialize(encoder: Encoder, value: Suspended) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PlatformBusinessStatus
}


private object PlatformBusinessStatusSerializer : KSerializer<PlatformBusinessStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformBusinessStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformBusinessStatus {
    val value = decoder.decodeString()
    return when (value) {
      "IN_BUSINESS" -> PlatformBusinessStatus.InBusiness
      "CLOSED" -> PlatformBusinessStatus.Closed
      "SUSPENDED" -> PlatformBusinessStatus.Suspended
      else -> PlatformBusinessStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformBusinessStatus) = encoder.encodeString(value.value)
}

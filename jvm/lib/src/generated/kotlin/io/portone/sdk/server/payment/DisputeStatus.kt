package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 분쟁 상태 */
@Serializable(DisputeStatusSerializer::class)
public sealed interface DisputeStatus {
  public val value: String
  /**
   * 분쟁 발생 상태
   *
   * 분쟁이 발생하였으며 아직 해소되지 않은 상태입니다.
   */
  @Serializable(UnresolvedSerializer::class)
  public data object Unresolved : DisputeStatus {
    override val value: String = "UNRESOLVED"
  }
  public object UnresolvedSerializer : KSerializer<Unresolved> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Unresolved::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Unresolved = decoder.decodeString().let {
      if (it != "UNRESOLVED") {
        throw SerializationException(it)
      } else {
        return Unresolved
      }
    }
    override fun serialize(encoder: Encoder, value: Unresolved): Unit = encoder.encodeString(value.value)
  }
  /**
   * 분쟁 해소 상태
   *
   * 분쟁이 발생하였으나 해소된 상태입니다.
   */
  @Serializable(ResolvedSerializer::class)
  public data object Resolved : DisputeStatus {
    override val value: String = "RESOLVED"
  }
  public object ResolvedSerializer : KSerializer<Resolved> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Resolved::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Resolved = decoder.decodeString().let {
      if (it != "RESOLVED") {
        throw SerializationException(it)
      } else {
        return Resolved
      }
    }
    override fun serialize(encoder: Encoder, value: Resolved): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : DisputeStatus
}


public object DisputeStatusSerializer : KSerializer<DisputeStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DisputeStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): DisputeStatus {
    val value = decoder.decodeString()
    return when (value) {
      "UNRESOLVED" -> DisputeStatus.Unresolved
      "RESOLVED" -> DisputeStatus.Resolved
      else -> DisputeStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: DisputeStatus): Unit = encoder.encodeString(value.value)
}

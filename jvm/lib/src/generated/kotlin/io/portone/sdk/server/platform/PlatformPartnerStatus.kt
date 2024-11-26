package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 파트너 상태 */
@Serializable(PlatformPartnerStatusSerializer::class)
public sealed interface PlatformPartnerStatus {
  public val value: String
  /** 승인 대기 중 */
  @Serializable(PendingSerializer::class)
  public data object Pending : PlatformPartnerStatus {
    override val value: String = "PENDING"
  }
  private object PendingSerializer : KSerializer<Pending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pending = decoder.decodeString().let {
      if (it != "PENDING") {
        throw SerializationException(it)
      } else {
        return Pending
      }
    }
    override fun serialize(encoder: Encoder, value: Pending) = encoder.encodeString(value.value)
  }
  /** 승인 완료 */
  @Serializable(ApprovedSerializer::class)
  public data object Approved : PlatformPartnerStatus {
    override val value: String = "APPROVED"
  }
  private object ApprovedSerializer : KSerializer<Approved> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Approved::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Approved = decoder.decodeString().let {
      if (it != "APPROVED") {
        throw SerializationException(it)
      } else {
        return Approved
      }
    }
    override fun serialize(encoder: Encoder, value: Approved) = encoder.encodeString(value.value)
  }
  /** 승인 거절 */
  @Serializable(RejectedSerializer::class)
  public data object Rejected : PlatformPartnerStatus {
    override val value: String = "REJECTED"
  }
  private object RejectedSerializer : KSerializer<Rejected> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Rejected::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Rejected = decoder.decodeString().let {
      if (it != "REJECTED") {
        throw SerializationException(it)
      } else {
        return Rejected
      }
    }
    override fun serialize(encoder: Encoder, value: Rejected) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerStatus
}


private object PlatformPartnerStatusSerializer : KSerializer<PlatformPartnerStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPartnerStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPartnerStatus {
    val value = decoder.decodeString()
    return when (value) {
      "PENDING" -> PlatformPartnerStatus.Pending
      "APPROVED" -> PlatformPartnerStatus.Approved
      "REJECTED" -> PlatformPartnerStatus.Rejected
      else -> PlatformPartnerStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPartnerStatus) = encoder.encodeString(value.value)
}

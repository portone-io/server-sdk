package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 파트너 사업자 상태 */
@Serializable(PlatformPartnerBusinessStatusSerializer::class)
public sealed interface PlatformPartnerBusinessStatus {
  public val value: String
  /** 인증 되지 않음 */
  @Serializable(NotVerifiedSerializer::class)
  public data object NotVerified : PlatformPartnerBusinessStatus {
    override val value: String = "NOT_VERIFIED"
  }
  private object NotVerifiedSerializer : KSerializer<NotVerified> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NotVerified::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NotVerified = decoder.decodeString().let {
      if (it != "NOT_VERIFIED") {
        throw SerializationException(it)
      } else {
        return NotVerified
      }
    }
    override fun serialize(encoder: Encoder, value: NotVerified) = encoder.encodeString(value.value)
  }
  /** 인증 실패 */
  @Serializable(VerifyFailedSerializer::class)
  public data object VerifyFailed : PlatformPartnerBusinessStatus {
    override val value: String = "VERIFY_FAILED"
  }
  private object VerifyFailedSerializer : KSerializer<VerifyFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(VerifyFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): VerifyFailed = decoder.decodeString().let {
      if (it != "VERIFY_FAILED") {
        throw SerializationException(it)
      } else {
        return VerifyFailed
      }
    }
    override fun serialize(encoder: Encoder, value: VerifyFailed) = encoder.encodeString(value.value)
  }
  /** 대응되는 사업자 없음 */
  @Serializable(NotFoundSerializer::class)
  public data object NotFound : PlatformPartnerBusinessStatus {
    override val value: String = "NOT_FOUND"
  }
  private object NotFoundSerializer : KSerializer<NotFound> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NotFound::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NotFound = decoder.decodeString().let {
      if (it != "NOT_FOUND") {
        throw SerializationException(it)
      } else {
        return NotFound
      }
    }
    override fun serialize(encoder: Encoder, value: NotFound) = encoder.encodeString(value.value)
  }
  /** 인증 대기 중 */
  @Serializable(VerifyingSerializer::class)
  public data object Verifying : PlatformPartnerBusinessStatus {
    override val value: String = "VERIFYING"
  }
  private object VerifyingSerializer : KSerializer<Verifying> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Verifying::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Verifying = decoder.decodeString().let {
      if (it != "VERIFYING") {
        throw SerializationException(it)
      } else {
        return Verifying
      }
    }
    override fun serialize(encoder: Encoder, value: Verifying) = encoder.encodeString(value.value)
  }
  /** 사업 중 */
  @Serializable(InBusinessSerializer::class)
  public data object InBusiness : PlatformPartnerBusinessStatus {
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
  public data object Closed : PlatformPartnerBusinessStatus {
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
  public data object Suspended : PlatformPartnerBusinessStatus {
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
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerBusinessStatus
}


private object PlatformPartnerBusinessStatusSerializer : KSerializer<PlatformPartnerBusinessStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPartnerBusinessStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPartnerBusinessStatus {
    val value = decoder.decodeString()
    return when (value) {
      "NOT_VERIFIED" -> PlatformPartnerBusinessStatus.NotVerified
      "VERIFY_FAILED" -> PlatformPartnerBusinessStatus.VerifyFailed
      "NOT_FOUND" -> PlatformPartnerBusinessStatus.NotFound
      "VERIFYING" -> PlatformPartnerBusinessStatus.Verifying
      "IN_BUSINESS" -> PlatformPartnerBusinessStatus.InBusiness
      "CLOSED" -> PlatformPartnerBusinessStatus.Closed
      "SUSPENDED" -> PlatformPartnerBusinessStatus.Suspended
      else -> PlatformPartnerBusinessStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPartnerBusinessStatus) = encoder.encodeString(value.value)
}

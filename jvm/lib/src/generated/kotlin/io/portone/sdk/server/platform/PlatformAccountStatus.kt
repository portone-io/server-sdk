package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 계좌 상태 */
@Serializable(PlatformAccountStatusSerializer::class)
public sealed interface PlatformAccountStatus {
  public val value: String
  /** 계좌 인증 중 */
  @Serializable(VerifyingSerializer::class)
  public data object Verifying : PlatformAccountStatus {
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
  /** 계좌 인증 완료됨 */
  @Serializable(VerifiedSerializer::class)
  public data object Verified : PlatformAccountStatus {
    override val value: String = "VERIFIED"
  }
  private object VerifiedSerializer : KSerializer<Verified> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Verified::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Verified = decoder.decodeString().let {
      if (it != "VERIFIED") {
        throw SerializationException(it)
      } else {
        return Verified
      }
    }
    override fun serialize(encoder: Encoder, value: Verified) = encoder.encodeString(value.value)
  }
  /** 계좌 인증 실패함 */
  @Serializable(VerifyFailedSerializer::class)
  public data object VerifyFailed : PlatformAccountStatus {
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
  /** 계좌 인증 안됨 */
  @Serializable(NotVerifiedSerializer::class)
  public data object NotVerified : PlatformAccountStatus {
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
  /** 계좌 인증 만료됨 */
  @Serializable(ExpiredSerializer::class)
  public data object Expired : PlatformAccountStatus {
    override val value: String = "EXPIRED"
  }
  private object ExpiredSerializer : KSerializer<Expired> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Expired::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Expired = decoder.decodeString().let {
      if (it != "EXPIRED") {
        throw SerializationException(it)
      } else {
        return Expired
      }
    }
    override fun serialize(encoder: Encoder, value: Expired) = encoder.encodeString(value.value)
  }
  /** 알 수 없는 상태 */
  @Serializable(UnknownSerializer::class)
  public data object Unknown : PlatformAccountStatus {
    override val value: String = "UNKNOWN"
  }
  private object UnknownSerializer : KSerializer<Unknown> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Unknown::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Unknown = decoder.decodeString().let {
      if (it != "UNKNOWN") {
        throw SerializationException(it)
      } else {
        return Unknown
      }
    }
    override fun serialize(encoder: Encoder, value: Unknown) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformAccountStatus
}


private object PlatformAccountStatusSerializer : KSerializer<PlatformAccountStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformAccountStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformAccountStatus {
    val value = decoder.decodeString()
    return when (value) {
      "VERIFYING" -> PlatformAccountStatus.Verifying
      "VERIFIED" -> PlatformAccountStatus.Verified
      "VERIFY_FAILED" -> PlatformAccountStatus.VerifyFailed
      "NOT_VERIFIED" -> PlatformAccountStatus.NotVerified
      "EXPIRED" -> PlatformAccountStatus.Expired
      "UNKNOWN" -> PlatformAccountStatus.Unknown
      else -> PlatformAccountStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformAccountStatus) = encoder.encodeString(value.value)
}

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
  /** 계좌 인증 완료됨 */
  @Serializable(VerifiedSerializer::class)
  public data object Verified : PlatformAccountStatus {
    override val value: String = "VERIFIED"
  }
  public object VerifiedSerializer : KSerializer<Verified> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Verified::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Verified = decoder.decodeString().let {
      if (it != "VERIFIED") {
        throw SerializationException(it)
      } else {
        return Verified
      }
    }
    override fun serialize(encoder: Encoder, value: Verified): Unit = encoder.encodeString(value.value)
  }
  /** 계좌주 불일치 */
  @Serializable(VerifyFailedSerializer::class)
  public data object VerifyFailed : PlatformAccountStatus {
    override val value: String = "VERIFY_FAILED"
  }
  public object VerifyFailedSerializer : KSerializer<VerifyFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(VerifyFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): VerifyFailed = decoder.decodeString().let {
      if (it != "VERIFY_FAILED") {
        throw SerializationException(it)
      } else {
        return VerifyFailed
      }
    }
    override fun serialize(encoder: Encoder, value: VerifyFailed): Unit = encoder.encodeString(value.value)
  }
  /** 계좌 인증 오류 */
  @Serializable(VerifyErrorSerializer::class)
  public data object VerifyError : PlatformAccountStatus {
    override val value: String = "VERIFY_ERROR"
  }
  public object VerifyErrorSerializer : KSerializer<VerifyError> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(VerifyError::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): VerifyError = decoder.decodeString().let {
      if (it != "VERIFY_ERROR") {
        throw SerializationException(it)
      } else {
        return VerifyError
      }
    }
    override fun serialize(encoder: Encoder, value: VerifyError): Unit = encoder.encodeString(value.value)
  }
  /** 계좌 인증 안됨 */
  @Serializable(NotVerifiedSerializer::class)
  public data object NotVerified : PlatformAccountStatus {
    override val value: String = "NOT_VERIFIED"
  }
  public object NotVerifiedSerializer : KSerializer<NotVerified> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NotVerified::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NotVerified = decoder.decodeString().let {
      if (it != "NOT_VERIFIED") {
        throw SerializationException(it)
      } else {
        return NotVerified
      }
    }
    override fun serialize(encoder: Encoder, value: NotVerified): Unit = encoder.encodeString(value.value)
  }
  /** 알 수 없는 상태 */
  @Serializable(UnknownSerializer::class)
  public data object Unknown : PlatformAccountStatus {
    override val value: String = "UNKNOWN"
  }
  public object UnknownSerializer : KSerializer<Unknown> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Unknown::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Unknown = decoder.decodeString().let {
      if (it != "UNKNOWN") {
        throw SerializationException(it)
      } else {
        return Unknown
      }
    }
    override fun serialize(encoder: Encoder, value: Unknown): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformAccountStatus
}


public object PlatformAccountStatusSerializer : KSerializer<PlatformAccountStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformAccountStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformAccountStatus {
    val value = decoder.decodeString()
    return when (value) {
      "VERIFIED" -> PlatformAccountStatus.Verified
      "VERIFY_FAILED" -> PlatformAccountStatus.VerifyFailed
      "VERIFY_ERROR" -> PlatformAccountStatus.VerifyError
      "NOT_VERIFIED" -> PlatformAccountStatus.NotVerified
      "UNKNOWN" -> PlatformAccountStatus.Unknown
      else -> PlatformAccountStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformAccountStatus): Unit = encoder.encodeString(value.value)
}

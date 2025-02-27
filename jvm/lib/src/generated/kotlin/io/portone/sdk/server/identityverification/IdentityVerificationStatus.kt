package io.portone.sdk.server.identityverification

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 본인인증 상태 */
@Serializable(IdentityVerificationStatusSerializer::class)
public sealed interface IdentityVerificationStatus {
  public val value: String
  /** 요청 상태 */
  @Serializable(ReadySerializer::class)
  public data object Ready : IdentityVerificationStatus {
    override val value: String = "READY"
  }
  private object ReadySerializer : KSerializer<Ready> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ready::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ready = decoder.decodeString().let {
      if (it != "READY") {
        throw SerializationException(it)
      } else {
        return Ready
      }
    }
    override fun serialize(encoder: Encoder, value: Ready) = encoder.encodeString(value.value)
  }
  /** 완료 상태 */
  @Serializable(VerifiedSerializer::class)
  public data object Verified : IdentityVerificationStatus {
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
  /** 실패 상태 */
  @Serializable(FailedSerializer::class)
  public data object Failed : IdentityVerificationStatus {
    override val value: String = "FAILED"
  }
  private object FailedSerializer : KSerializer<Failed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Failed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Failed = decoder.decodeString().let {
      if (it != "FAILED") {
        throw SerializationException(it)
      } else {
        return Failed
      }
    }
    override fun serialize(encoder: Encoder, value: Failed) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : IdentityVerificationStatus
}


private object IdentityVerificationStatusSerializer : KSerializer<IdentityVerificationStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IdentityVerificationStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): IdentityVerificationStatus {
    val value = decoder.decodeString()
    return when (value) {
      "READY" -> IdentityVerificationStatus.Ready
      "VERIFIED" -> IdentityVerificationStatus.Verified
      "FAILED" -> IdentityVerificationStatus.Failed
      else -> IdentityVerificationStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: IdentityVerificationStatus) = encoder.encodeString(value.value)
}

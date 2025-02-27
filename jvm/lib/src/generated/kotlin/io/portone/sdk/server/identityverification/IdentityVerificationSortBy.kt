package io.portone.sdk.server.identityverification

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 본인인증 내역 정렬 기준 */
@Serializable(IdentityVerificationSortBySerializer::class)
public sealed interface IdentityVerificationSortBy {
  public val value: String
  /** 요청 시각 */
  @Serializable(RequestedAtSerializer::class)
  public data object RequestedAt : IdentityVerificationSortBy {
    override val value: String = "REQUESTED_AT"
  }
  private object RequestedAtSerializer : KSerializer<RequestedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(RequestedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): RequestedAt = decoder.decodeString().let {
      if (it != "REQUESTED_AT") {
        throw SerializationException(it)
      } else {
        return RequestedAt
      }
    }
    override fun serialize(encoder: Encoder, value: RequestedAt) = encoder.encodeString(value.value)
  }
  /** 완료 시각 */
  @Serializable(VerifiedAtSerializer::class)
  public data object VerifiedAt : IdentityVerificationSortBy {
    override val value: String = "VERIFIED_AT"
  }
  private object VerifiedAtSerializer : KSerializer<VerifiedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(VerifiedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): VerifiedAt = decoder.decodeString().let {
      if (it != "VERIFIED_AT") {
        throw SerializationException(it)
      } else {
        return VerifiedAt
      }
    }
    override fun serialize(encoder: Encoder, value: VerifiedAt) = encoder.encodeString(value.value)
  }
  /** 실패 시각 */
  @Serializable(FailedAtSerializer::class)
  public data object FailedAt : IdentityVerificationSortBy {
    override val value: String = "FAILED_AT"
  }
  private object FailedAtSerializer : KSerializer<FailedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(FailedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): FailedAt = decoder.decodeString().let {
      if (it != "FAILED_AT") {
        throw SerializationException(it)
      } else {
        return FailedAt
      }
    }
    override fun serialize(encoder: Encoder, value: FailedAt) = encoder.encodeString(value.value)
  }
  /**
   * 상태 변경 시각
   *
   * 요청 상태의 경우 REQUESTED_AT, 완료 상태의 경우 VERIFIED_AT, 실패 상태의 경우 FAILED_AT
   */
  @Serializable(StatusUpdatedAtSerializer::class)
  public data object StatusUpdatedAt : IdentityVerificationSortBy {
    override val value: String = "STATUS_UPDATED_AT"
  }
  private object StatusUpdatedAtSerializer : KSerializer<StatusUpdatedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(StatusUpdatedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): StatusUpdatedAt = decoder.decodeString().let {
      if (it != "STATUS_UPDATED_AT") {
        throw SerializationException(it)
      } else {
        return StatusUpdatedAt
      }
    }
    override fun serialize(encoder: Encoder, value: StatusUpdatedAt) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : IdentityVerificationSortBy
}


private object IdentityVerificationSortBySerializer : KSerializer<IdentityVerificationSortBy> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IdentityVerificationSortBy::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): IdentityVerificationSortBy {
    val value = decoder.decodeString()
    return when (value) {
      "REQUESTED_AT" -> IdentityVerificationSortBy.RequestedAt
      "VERIFIED_AT" -> IdentityVerificationSortBy.VerifiedAt
      "FAILED_AT" -> IdentityVerificationSortBy.FailedAt
      "STATUS_UPDATED_AT" -> IdentityVerificationSortBy.StatusUpdatedAt
      else -> IdentityVerificationSortBy.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: IdentityVerificationSortBy) = encoder.encodeString(value.value)
}

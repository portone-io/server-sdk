package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 빌링키 정렬 기준 */
@Serializable(BillingKeySortBySerializer::class)
public sealed interface BillingKeySortBy {
  public val value: String
  /** 발급 요청 시각 */
  @Serializable(RequestedAtSerializer::class)
  public data object RequestedAt : BillingKeySortBy {
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
  /** 발급 완료 시각 */
  @Serializable(IssuedAtSerializer::class)
  public data object IssuedAt : BillingKeySortBy {
    override val value: String = "ISSUED_AT"
  }
  private object IssuedAtSerializer : KSerializer<IssuedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IssuedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): IssuedAt = decoder.decodeString().let {
      if (it != "ISSUED_AT") {
        throw SerializationException(it)
      } else {
        return IssuedAt
      }
    }
    override fun serialize(encoder: Encoder, value: IssuedAt) = encoder.encodeString(value.value)
  }
  /** 삭제 완료 시각 */
  @Serializable(DeletedAtSerializer::class)
  public data object DeletedAt : BillingKeySortBy {
    override val value: String = "DELETED_AT"
  }
  private object DeletedAtSerializer : KSerializer<DeletedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DeletedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DeletedAt = decoder.decodeString().let {
      if (it != "DELETED_AT") {
        throw SerializationException(it)
      } else {
        return DeletedAt
      }
    }
    override fun serialize(encoder: Encoder, value: DeletedAt) = encoder.encodeString(value.value)
  }
  /**
   * 상태 변경 시각
   *
   * 발급 완료 상태의 경우 ISSUED_AT, 삭제 완료 상태의 경우 DELETED_AT
   */
  @Serializable(StatusTimestampSerializer::class)
  public data object StatusTimestamp : BillingKeySortBy {
    override val value: String = "STATUS_TIMESTAMP"
  }
  private object StatusTimestampSerializer : KSerializer<StatusTimestamp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(StatusTimestamp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): StatusTimestamp = decoder.decodeString().let {
      if (it != "STATUS_TIMESTAMP") {
        throw SerializationException(it)
      } else {
        return StatusTimestamp
      }
    }
    override fun serialize(encoder: Encoder, value: StatusTimestamp) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : BillingKeySortBy
}


private object BillingKeySortBySerializer : KSerializer<BillingKeySortBy> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BillingKeySortBy::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): BillingKeySortBy {
    val value = decoder.decodeString()
    return when (value) {
      "REQUESTED_AT" -> BillingKeySortBy.RequestedAt
      "ISSUED_AT" -> BillingKeySortBy.IssuedAt
      "DELETED_AT" -> BillingKeySortBy.DeletedAt
      "STATUS_TIMESTAMP" -> BillingKeySortBy.StatusTimestamp
      else -> BillingKeySortBy.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: BillingKeySortBy) = encoder.encodeString(value.value)
}

package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제 건 정렬 기준 */
@Serializable(PaymentSortBySerializer::class)
public sealed interface PaymentSortBy {
  public val value: String
  /** 결제 요청 시점 */
  @Serializable(RequestedAtSerializer::class)
  public data object RequestedAt : PaymentSortBy {
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
  /** 상태 변경 시점 */
  @Serializable(StatusChangedAtSerializer::class)
  public data object StatusChangedAt : PaymentSortBy {
    override val value: String = "STATUS_CHANGED_AT"
  }
  private object StatusChangedAtSerializer : KSerializer<StatusChangedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(StatusChangedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): StatusChangedAt = decoder.decodeString().let {
      if (it != "STATUS_CHANGED_AT") {
        throw SerializationException(it)
      } else {
        return StatusChangedAt
      }
    }
    override fun serialize(encoder: Encoder, value: StatusChangedAt) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PaymentSortBy
}


private object PaymentSortBySerializer : KSerializer<PaymentSortBy> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentSortBy::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentSortBy {
    val value = decoder.decodeString()
    return when (value) {
      "REQUESTED_AT" -> PaymentSortBy.RequestedAt
      "STATUS_CHANGED_AT" -> PaymentSortBy.StatusChangedAt
      else -> PaymentSortBy.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentSortBy) = encoder.encodeString(value.value)
}

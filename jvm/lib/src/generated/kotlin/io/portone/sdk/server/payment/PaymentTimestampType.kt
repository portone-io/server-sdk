package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/**
 * 조회 시점 기준
 *
 * 어떤 시점을 기준으로 조회를 할 것인지 선택합니다.
 * CREATED_AT: 결제 건 생성 시점을 기준으로 조회합니다.
 * STATUS_CHANGED_AT: 상태 승인 시점을 기준으로 조회합니다. 결제 건의 최종 상태에 따라 검색 기준이 다르게 적용됩니다.
 * ready -> 결제 요청 시점 기준
 * paid -> 결제 완료 시점 기준
 * cancelled -> 결제 취소 시점 기준
 * failed -> 결제 실패 시점 기준
 * 값을 입력하지 않으면 STATUS_CHANGED_AT 으로 자동 적용됩니다.
 */
@Serializable(PaymentTimestampTypeSerializer::class)
public sealed interface PaymentTimestampType {
  public val value: String
  /** 결제 건 생성 시점 */
  @Serializable(CreatedAtSerializer::class)
  public data object CreatedAt : PaymentTimestampType {
    override val value: String = "CREATED_AT"
  }
  private object CreatedAtSerializer : KSerializer<CreatedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CreatedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CreatedAt = decoder.decodeString().let {
      if (it != "CREATED_AT") {
        throw SerializationException(it)
      } else {
        return CreatedAt
      }
    }
    override fun serialize(encoder: Encoder, value: CreatedAt) = encoder.encodeString(value.value)
  }
  /** 상태 변경 시점 */
  @Serializable(StatusChangedAtSerializer::class)
  public data object StatusChangedAt : PaymentTimestampType {
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
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentTimestampType
}


private object PaymentTimestampTypeSerializer : KSerializer<PaymentTimestampType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentTimestampType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentTimestampType {
    val value = decoder.decodeString()
    return when (value) {
      "CREATED_AT" -> PaymentTimestampType.CreatedAt
      "STATUS_CHANGED_AT" -> PaymentTimestampType.StatusChangedAt
      else -> PaymentTimestampType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentTimestampType) = encoder.encodeString(value.value)
}

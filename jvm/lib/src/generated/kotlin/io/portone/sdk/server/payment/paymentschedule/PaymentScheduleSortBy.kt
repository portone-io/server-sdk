package io.portone.sdk.server.payment.paymentschedule

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제 예약 건 정렬 기준 */
@Serializable(PaymentScheduleSortBySerializer::class)
public sealed interface PaymentScheduleSortBy {
  public val value: String
  /** 결제 예약 생성 시각 */
  @Serializable(CreatedAtSerializer::class)
  public data object CreatedAt : PaymentScheduleSortBy {
    override val value: String = "CREATED_AT"
  }
  public object CreatedAtSerializer : KSerializer<CreatedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CreatedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CreatedAt = decoder.decodeString().let {
      if (it != "CREATED_AT") {
        throw SerializationException(it)
      } else {
        return CreatedAt
      }
    }
    override fun serialize(encoder: Encoder, value: CreatedAt): Unit = encoder.encodeString(value.value)
  }
  /** 결제 예정 시각 */
  @Serializable(TimeToPaySerializer::class)
  public data object TimeToPay : PaymentScheduleSortBy {
    override val value: String = "TIME_TO_PAY"
  }
  public object TimeToPaySerializer : KSerializer<TimeToPay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TimeToPay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TimeToPay = decoder.decodeString().let {
      if (it != "TIME_TO_PAY") {
        throw SerializationException(it)
      } else {
        return TimeToPay
      }
    }
    override fun serialize(encoder: Encoder, value: TimeToPay): Unit = encoder.encodeString(value.value)
  }
  /** 예약 결제 시도(성공 / 실패) 시각 */
  @Serializable(CompletedAtSerializer::class)
  public data object CompletedAt : PaymentScheduleSortBy {
    override val value: String = "COMPLETED_AT"
  }
  public object CompletedAtSerializer : KSerializer<CompletedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CompletedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CompletedAt = decoder.decodeString().let {
      if (it != "COMPLETED_AT") {
        throw SerializationException(it)
      } else {
        return CompletedAt
      }
    }
    override fun serialize(encoder: Encoder, value: CompletedAt): Unit = encoder.encodeString(value.value)
  }
  /** 결제 시도 또는 예정 시각. 해지 건은 해지 시각. */
  @Serializable(StatusTimestampSerializer::class)
  public data object StatusTimestamp : PaymentScheduleSortBy {
    override val value: String = "STATUS_TIMESTAMP"
  }
  public object StatusTimestampSerializer : KSerializer<StatusTimestamp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(StatusTimestamp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): StatusTimestamp = decoder.decodeString().let {
      if (it != "STATUS_TIMESTAMP") {
        throw SerializationException(it)
      } else {
        return StatusTimestamp
      }
    }
    override fun serialize(encoder: Encoder, value: StatusTimestamp): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentScheduleSortBy
}


public object PaymentScheduleSortBySerializer : KSerializer<PaymentScheduleSortBy> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentScheduleSortBy::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentScheduleSortBy {
    val value = decoder.decodeString()
    return when (value) {
      "CREATED_AT" -> PaymentScheduleSortBy.CreatedAt
      "TIME_TO_PAY" -> PaymentScheduleSortBy.TimeToPay
      "COMPLETED_AT" -> PaymentScheduleSortBy.CompletedAt
      "STATUS_TIMESTAMP" -> PaymentScheduleSortBy.StatusTimestamp
      else -> PaymentScheduleSortBy.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentScheduleSortBy): Unit = encoder.encodeString(value.value)
}

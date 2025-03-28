package io.portone.sdk.server.payment.paymentschedule

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제 예약 건 상태 */
@Serializable(PaymentScheduleStatusSerializer::class)
public sealed interface PaymentScheduleStatus {
  public val value: String
  /** 예약 완료 */
  @Serializable(ScheduledSerializer::class)
  public data object Scheduled : PaymentScheduleStatus {
    override val value: String = "SCHEDULED"
  }
  private object ScheduledSerializer : KSerializer<Scheduled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Scheduled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Scheduled = decoder.decodeString().let {
      if (it != "SCHEDULED") {
        throw SerializationException(it)
      } else {
        return Scheduled
      }
    }
    override fun serialize(encoder: Encoder, value: Scheduled) = encoder.encodeString(value.value)
  }
  /** 결제 시작 */
  @Serializable(StartedSerializer::class)
  public data object Started : PaymentScheduleStatus {
    override val value: String = "STARTED"
  }
  private object StartedSerializer : KSerializer<Started> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Started::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Started = decoder.decodeString().let {
      if (it != "STARTED") {
        throw SerializationException(it)
      } else {
        return Started
      }
    }
    override fun serialize(encoder: Encoder, value: Started) = encoder.encodeString(value.value)
  }
  /** 결제 성공 */
  @Serializable(SucceededSerializer::class)
  public data object Succeeded : PaymentScheduleStatus {
    override val value: String = "SUCCEEDED"
  }
  private object SucceededSerializer : KSerializer<Succeeded> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Succeeded::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Succeeded = decoder.decodeString().let {
      if (it != "SUCCEEDED") {
        throw SerializationException(it)
      } else {
        return Succeeded
      }
    }
    override fun serialize(encoder: Encoder, value: Succeeded) = encoder.encodeString(value.value)
  }
  /** 결제 실패 */
  @Serializable(FailedSerializer::class)
  public data object Failed : PaymentScheduleStatus {
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
  /** 취소된 결제 예약 */
  @Serializable(RevokedSerializer::class)
  public data object Revoked : PaymentScheduleStatus {
    override val value: String = "REVOKED"
  }
  private object RevokedSerializer : KSerializer<Revoked> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Revoked::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Revoked = decoder.decodeString().let {
      if (it != "REVOKED") {
        throw SerializationException(it)
      } else {
        return Revoked
      }
    }
    override fun serialize(encoder: Encoder, value: Revoked) = encoder.encodeString(value.value)
  }
  /** 결제 승인 대기 */
  @Serializable(PendingSerializer::class)
  public data object Pending : PaymentScheduleStatus {
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
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PaymentScheduleStatus
}


private object PaymentScheduleStatusSerializer : KSerializer<PaymentScheduleStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentScheduleStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentScheduleStatus {
    val value = decoder.decodeString()
    return when (value) {
      "SCHEDULED" -> PaymentScheduleStatus.Scheduled
      "STARTED" -> PaymentScheduleStatus.Started
      "SUCCEEDED" -> PaymentScheduleStatus.Succeeded
      "FAILED" -> PaymentScheduleStatus.Failed
      "REVOKED" -> PaymentScheduleStatus.Revoked
      "PENDING" -> PaymentScheduleStatus.Pending
      else -> PaymentScheduleStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentScheduleStatus) = encoder.encodeString(value.value)
}

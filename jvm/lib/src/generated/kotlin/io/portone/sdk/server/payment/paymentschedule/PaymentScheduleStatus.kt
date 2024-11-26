package io.portone.sdk.server.payment.paymentschedule

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
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
  public data object Scheduled : PaymentScheduleStatus {
    override val value: String = "SCHEDULED"
  }
  /** 결제 시작 */
  public data object Started : PaymentScheduleStatus {
    override val value: String = "STARTED"
  }
  /** 결제 성공 */
  public data object Succeeded : PaymentScheduleStatus {
    override val value: String = "SUCCEEDED"
  }
  /** 결제 실패 */
  public data object Failed : PaymentScheduleStatus {
    override val value: String = "FAILED"
  }
  /** 취소된 결제 예약 */
  public data object Revoked : PaymentScheduleStatus {
    override val value: String = "REVOKED"
  }
  /** 결제 승인 대기 */
  public data object Pending : PaymentScheduleStatus {
    override val value: String = "PENDING"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentScheduleStatus
}


private object PaymentScheduleStatusSerializer : KSerializer<PaymentScheduleStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentScheduleStatus::class.java.canonicalName, PrimitiveKind.STRING)
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

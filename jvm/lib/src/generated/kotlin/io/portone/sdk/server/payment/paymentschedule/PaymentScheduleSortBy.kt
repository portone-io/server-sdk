package io.portone.sdk.server.payment.paymentschedule

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
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
  public data object CreatedAt : PaymentScheduleSortBy {
    override val value: String = "CREATED_AT"
  }
  /** 결제 예정 시각 */
  public data object TimeToPay : PaymentScheduleSortBy {
    override val value: String = "TIME_TO_PAY"
  }
  /** 예약 결제 시도(성공 / 실패) 시각 */
  public data object CompletedAt : PaymentScheduleSortBy {
    override val value: String = "COMPLETED_AT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentScheduleSortBy
}


private object PaymentScheduleSortBySerializer : KSerializer<PaymentScheduleSortBy> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentScheduleSortBy::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentScheduleSortBy {
    val value = decoder.decodeString()
    return when (value) {
      "CREATED_AT" -> PaymentScheduleSortBy.CreatedAt
      "TIME_TO_PAY" -> PaymentScheduleSortBy.TimeToPay
      "COMPLETED_AT" -> PaymentScheduleSortBy.CompletedAt
      else -> PaymentScheduleSortBy.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentScheduleSortBy) = encoder.encodeString(value.value)
}

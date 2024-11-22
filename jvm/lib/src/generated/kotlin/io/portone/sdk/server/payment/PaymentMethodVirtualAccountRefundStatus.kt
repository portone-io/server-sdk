package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 가상계좌 환불 상태 */
@Serializable(PaymentMethodVirtualAccountRefundStatusSerializer::class)
public sealed interface PaymentMethodVirtualAccountRefundStatus {
  public val value: String
  /** 처리중 */
  public data object Pending : PaymentMethodVirtualAccountRefundStatus {
    override val value: String = "PENDING"
  }
  /** 부분 환불 실패 */
  public data object PartialRefundFailed : PaymentMethodVirtualAccountRefundStatus {
    override val value: String = "PARTIAL_REFUND_FAILED"
  }
  /** 환불 실패 */
  public data object Failed : PaymentMethodVirtualAccountRefundStatus {
    override val value: String = "FAILED"
  }
  /** 환불 완료 */
  public data object Completed : PaymentMethodVirtualAccountRefundStatus {
    override val value: String = "COMPLETED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentMethodVirtualAccountRefundStatus
}


private object PaymentMethodVirtualAccountRefundStatusSerializer : KSerializer<PaymentMethodVirtualAccountRefundStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentMethodVirtualAccountRefundStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentMethodVirtualAccountRefundStatus {
    val value = decoder.decodeString()
    return when (value) {
      "PENDING" -> PaymentMethodVirtualAccountRefundStatus.Pending
      "PARTIAL_REFUND_FAILED" -> PaymentMethodVirtualAccountRefundStatus.PartialRefundFailed
      "FAILED" -> PaymentMethodVirtualAccountRefundStatus.Failed
      "COMPLETED" -> PaymentMethodVirtualAccountRefundStatus.Completed
      else -> PaymentMethodVirtualAccountRefundStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentMethodVirtualAccountRefundStatus) = encoder.encodeString(value.value)
}

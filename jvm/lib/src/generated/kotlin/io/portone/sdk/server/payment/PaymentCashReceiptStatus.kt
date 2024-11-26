package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제건 내 현금영수증 상태 */
@Serializable(PaymentCashReceiptStatusSerializer::class)
public sealed interface PaymentCashReceiptStatus {
  public val value: String
  public data object Issued : PaymentCashReceiptStatus {
    override val value: String = "ISSUED"
  }
  public data object Cancelled : PaymentCashReceiptStatus {
    override val value: String = "CANCELLED"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentCashReceiptStatus
}


private object PaymentCashReceiptStatusSerializer : KSerializer<PaymentCashReceiptStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentCashReceiptStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentCashReceiptStatus {
    val value = decoder.decodeString()
    return when (value) {
      "ISSUED" -> PaymentCashReceiptStatus.Issued
      "CANCELLED" -> PaymentCashReceiptStatus.Cancelled
      else -> PaymentCashReceiptStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentCashReceiptStatus) = encoder.encodeString(value.value)
}

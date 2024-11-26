package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 빌링키 결제 수단 */
@Serializable(BillingKeyPaymentMethodTypeSerializer::class)
public sealed interface BillingKeyPaymentMethodType {
  public val value: String
  /** 카드 */
  public data object Card : BillingKeyPaymentMethodType {
    override val value: String = "CARD"
  }
  /** 모바일 */
  public data object Mobile : BillingKeyPaymentMethodType {
    override val value: String = "MOBILE"
  }
  /** 간편 결제 */
  public data object EasyPay : BillingKeyPaymentMethodType {
    override val value: String = "EASY_PAY"
  }
  /** 계좌 이체 */
  public data object Transfer : BillingKeyPaymentMethodType {
    override val value: String = "TRANSFER"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : BillingKeyPaymentMethodType
}


private object BillingKeyPaymentMethodTypeSerializer : KSerializer<BillingKeyPaymentMethodType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BillingKeyPaymentMethodType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): BillingKeyPaymentMethodType {
    val value = decoder.decodeString()
    return when (value) {
      "CARD" -> BillingKeyPaymentMethodType.Card
      "MOBILE" -> BillingKeyPaymentMethodType.Mobile
      "EASY_PAY" -> BillingKeyPaymentMethodType.EasyPay
      "TRANSFER" -> BillingKeyPaymentMethodType.Transfer
      else -> BillingKeyPaymentMethodType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: BillingKeyPaymentMethodType) = encoder.encodeString(value.value)
}

package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/**
 * 에스크로 정보
 *
 * V1 결제 건의 경우 타입이 REGISTERED 로 고정됩니다.
 */
@Serializable(PaymentEscrowSerializer::class)
public sealed interface PaymentEscrow {
  @Serializable
  @JsonClassDiscriminator("status")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PaymentEscrow {
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PaymentEscrow
}


private object PaymentEscrowSerializer : JsonContentPolymorphicSerializer<PaymentEscrow>(PaymentEscrow::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["status"]?.jsonPrimitive?.contentOrNull) {
    "BEFORE_REGISTERED" -> BeforeRegisteredPaymentEscrow.serializer()
    "CANCELLED" -> CancelledPaymentEscrow.serializer()
    "CONFIRMED" -> ConfirmedPaymentEscrow.serializer()
    "DELIVERED" -> DeliveredPaymentEscrow.serializer()
    "REGISTERED" -> RegisteredPaymentEscrow.serializer()
    "REJECTED" -> RejectedPaymentEscrow.serializer()
    "REJECT_CONFIRMED" -> RejectConfirmedPaymentEscrow.serializer()
    else -> PaymentEscrow.Unrecognized.serializer()
  }
}

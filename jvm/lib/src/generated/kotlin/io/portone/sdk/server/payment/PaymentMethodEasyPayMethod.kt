package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 간편 결제 수단 */
@Serializable(PaymentMethodEasyPayMethodSerializer::class)
public sealed interface PaymentMethodEasyPayMethod {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : PaymentMethodEasyPayMethod {
  }
  @Serializable
  public data object Unrecognized : PaymentMethodEasyPayMethod
}


private object PaymentMethodEasyPayMethodSerializer : JsonContentPolymorphicSerializer<PaymentMethodEasyPayMethod>(PaymentMethodEasyPayMethod::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "PaymentMethodCard" -> PaymentMethodCard.serializer()
    "PaymentMethodEasyPayMethodCharge" -> PaymentMethodEasyPayMethodCharge.serializer()
    "PaymentMethodTransfer" -> PaymentMethodTransfer.serializer()
    else -> PaymentMethodEasyPayMethod.Unrecognized.serializer()
  }
}

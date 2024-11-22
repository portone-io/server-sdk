package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 결제수단 정보 */
@Serializable(PaymentMethodSerializer::class)
public sealed interface PaymentMethod {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : PaymentMethod {
  }
  @Serializable
  public data object Unrecognized : PaymentMethod
}


private object PaymentMethodSerializer : JsonContentPolymorphicSerializer<PaymentMethod>(PaymentMethod::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "PaymentMethodCard" -> PaymentMethodCard.serializer()
    "PaymentMethodEasyPay" -> PaymentMethodEasyPay.serializer()
    "PaymentMethodGiftCertificate" -> PaymentMethodGiftCertificate.serializer()
    "PaymentMethodMobile" -> PaymentMethodMobile.serializer()
    "PaymentMethodTransfer" -> PaymentMethodTransfer.serializer()
    "PaymentMethodVirtualAccount" -> PaymentMethodVirtualAccount.serializer()
    else -> PaymentMethod.Unrecognized.serializer()
  }
}

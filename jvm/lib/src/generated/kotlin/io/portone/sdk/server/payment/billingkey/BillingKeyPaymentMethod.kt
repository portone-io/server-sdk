package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 빌링키 발급 수단 정보 */
@Serializable(BillingKeyPaymentMethodSerializer::class)
public sealed interface BillingKeyPaymentMethod {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : BillingKeyPaymentMethod {
  }
  @Serializable
  public data object Unrecognized : BillingKeyPaymentMethod
}


private object BillingKeyPaymentMethodSerializer : JsonContentPolymorphicSerializer<BillingKeyPaymentMethod>(BillingKeyPaymentMethod::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "BillingKeyPaymentMethodCard" -> BillingKeyPaymentMethodCard.serializer()
    "BillingKeyPaymentMethodEasyPay" -> BillingKeyPaymentMethodEasyPay.serializer()
    "BillingKeyPaymentMethodMobile" -> BillingKeyPaymentMethodMobile.serializer()
    "BillingKeyPaymentMethodPaypal" -> BillingKeyPaymentMethodPaypal.serializer()
    "BillingKeyPaymentMethodTransfer" -> BillingKeyPaymentMethodTransfer.serializer()
    else -> BillingKeyPaymentMethod.Unrecognized.serializer()
  }
}

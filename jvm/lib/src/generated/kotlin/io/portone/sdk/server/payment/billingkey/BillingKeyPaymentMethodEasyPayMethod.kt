package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 간편 결제 수단 */
@Serializable(BillingKeyPaymentMethodEasyPayMethodSerializer::class)
public sealed interface BillingKeyPaymentMethodEasyPayMethod {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : BillingKeyPaymentMethodEasyPayMethod {
  }
  @Serializable
  public data object Unrecognized : BillingKeyPaymentMethodEasyPayMethod
}


private object BillingKeyPaymentMethodEasyPayMethodSerializer : JsonContentPolymorphicSerializer<BillingKeyPaymentMethodEasyPayMethod>(BillingKeyPaymentMethodEasyPayMethod::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "BillingKeyPaymentMethodCard" -> BillingKeyPaymentMethodCard.serializer()
    "BillingKeyPaymentMethodEasyPayCharge" -> BillingKeyPaymentMethodEasyPayCharge.serializer()
    "BillingKeyPaymentMethodTransfer" -> BillingKeyPaymentMethodTransfer.serializer()
    else -> BillingKeyPaymentMethodEasyPayMethod.Unrecognized.serializer()
  }
}

package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.KSerializer
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
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : BillingKeyPaymentMethod {
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : BillingKeyPaymentMethod
}


public object BillingKeyPaymentMethodSerializer : JsonContentPolymorphicSerializer<BillingKeyPaymentMethod>(BillingKeyPaymentMethod::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out BillingKeyPaymentMethod> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "BillingKeyPaymentMethodCard" -> BillingKeyPaymentMethodCard.serializer()
      "BillingKeyPaymentMethodEasyPay" -> BillingKeyPaymentMethodEasyPay.serializer()
      "BillingKeyPaymentMethodMobile" -> BillingKeyPaymentMethodMobile.serializer()
      "BillingKeyPaymentMethodPaypal" -> BillingKeyPaymentMethodPaypal.serializer()
      "BillingKeyPaymentMethodTransfer" -> BillingKeyPaymentMethodTransfer.serializer()
      else -> BillingKeyPaymentMethod.Unrecognized.serializer()
    }
}

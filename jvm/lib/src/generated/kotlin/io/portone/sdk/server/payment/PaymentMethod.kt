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
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PaymentMethod {
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PaymentMethod
}


private object PaymentMethodSerializer : JsonContentPolymorphicSerializer<PaymentMethod>(PaymentMethod::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "PaymentMethodCard" -> PaymentMethodCard.serializer()
    "PaymentMethodConvenienceStore" -> PaymentMethodConvenienceStore.serializer()
    "PaymentMethodCrypto" -> PaymentMethodCrypto.serializer()
    "PaymentMethodEasyPay" -> PaymentMethodEasyPay.serializer()
    "PaymentMethodGiftCertificate" -> PaymentMethodGiftCertificate.serializer()
    "PaymentMethodMobile" -> PaymentMethodMobile.serializer()
    "PaymentMethodTransfer" -> PaymentMethodTransfer.serializer()
    "PaymentMethodVirtualAccount" -> PaymentMethodVirtualAccount.serializer()
    else -> PaymentMethod.Unrecognized.serializer()
  }
}

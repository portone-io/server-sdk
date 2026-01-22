package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
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
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PaymentMethodEasyPayMethod {
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PaymentMethodEasyPayMethod
}


public object PaymentMethodEasyPayMethodSerializer : JsonContentPolymorphicSerializer<PaymentMethodEasyPayMethod>(PaymentMethodEasyPayMethod::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out PaymentMethodEasyPayMethod> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "PaymentMethodCard" -> PaymentMethodCard.serializer()
      "PaymentMethodEasyPayMethodCharge" -> PaymentMethodEasyPayMethodCharge.serializer()
      "PaymentMethodTransfer" -> PaymentMethodTransfer.serializer()
      else -> PaymentMethodEasyPayMethod.Unrecognized.serializer()
    }
}

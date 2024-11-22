package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 결제 수단 */
@Serializable(PlatformPaymentMethodSerializer::class)
public sealed interface PlatformPaymentMethod {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : PlatformPaymentMethod {
  }
  @Serializable
  public data object Unrecognized : PlatformPaymentMethod
}


private object PlatformPaymentMethodSerializer : JsonContentPolymorphicSerializer<PlatformPaymentMethod>(PlatformPaymentMethod::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "CARD" -> PlatformPaymentMethodCard.serializer()
    "EASY_PAY" -> PlatformPaymentMethodEasyPay.serializer()
    "GIFT_CERTIFICATE" -> PlatformPaymentMethodGiftCertificate.serializer()
    "MOBILE" -> PlatformPaymentMethodMobile.serializer()
    "TRANSFER" -> PlatformPaymentMethodTransfer.serializer()
    "VIRTUAL_ACCOUNT" -> PlatformPaymentMethodVirtualAccount.serializer()
    else -> PlatformPaymentMethod.Unrecognized.serializer()
  }
}

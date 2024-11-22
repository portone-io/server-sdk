package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetKakaopayPaymentOrderErrorSerializer::class)
public sealed interface GetKakaopayPaymentOrderError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetKakaopayPaymentOrderError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetKakaopayPaymentOrderError
}


private object GetKakaopayPaymentOrderErrorSerializer : JsonContentPolymorphicSerializer<GetKakaopayPaymentOrderError>(GetKakaopayPaymentOrderError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetKakaopayPaymentOrderError.Unrecognized.serializer()
  }
}

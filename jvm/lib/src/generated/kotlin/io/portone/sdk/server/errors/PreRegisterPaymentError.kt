package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(PreRegisterPaymentErrorSerializer::class)
public sealed interface PreRegisterPaymentError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : PreRegisterPaymentError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : PreRegisterPaymentError
}


private object PreRegisterPaymentErrorSerializer : JsonContentPolymorphicSerializer<PreRegisterPaymentError>(PreRegisterPaymentError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "ALREADY_PAID" -> AlreadyPaidError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> PreRegisterPaymentError.Unrecognized.serializer()
  }
}

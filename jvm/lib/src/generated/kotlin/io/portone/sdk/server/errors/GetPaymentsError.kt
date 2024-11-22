package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetPaymentsErrorSerializer::class)
public sealed interface GetPaymentsError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetPaymentsError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetPaymentsError
}


private object GetPaymentsErrorSerializer : JsonContentPolymorphicSerializer<GetPaymentsError>(GetPaymentsError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetPaymentsError.Unrecognized.serializer()
  }
}

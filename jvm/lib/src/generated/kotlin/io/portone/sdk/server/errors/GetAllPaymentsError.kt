package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetAllPaymentsErrorSerializer::class)
public sealed interface GetAllPaymentsError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetAllPaymentsError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetAllPaymentsError
}


private object GetAllPaymentsErrorSerializer : JsonContentPolymorphicSerializer<GetAllPaymentsError>(GetAllPaymentsError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetAllPaymentsError.Unrecognized.serializer()
  }
}

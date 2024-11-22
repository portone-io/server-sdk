package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetBillingKeyInfosErrorSerializer::class)
public sealed interface GetBillingKeyInfosError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetBillingKeyInfosError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetBillingKeyInfosError
}


private object GetBillingKeyInfosErrorSerializer : JsonContentPolymorphicSerializer<GetBillingKeyInfosError>(GetBillingKeyInfosError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetBillingKeyInfosError.Unrecognized.serializer()
  }
}

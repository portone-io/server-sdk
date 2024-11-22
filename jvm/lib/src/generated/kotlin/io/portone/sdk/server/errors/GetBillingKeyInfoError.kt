package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetBillingKeyInfoErrorSerializer::class)
public sealed interface GetBillingKeyInfoError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetBillingKeyInfoError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetBillingKeyInfoError
}


private object GetBillingKeyInfoErrorSerializer : JsonContentPolymorphicSerializer<GetBillingKeyInfoError>(GetBillingKeyInfoError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "BILLING_KEY_NOT_FOUND" -> BillingKeyNotFoundError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetBillingKeyInfoError.Unrecognized.serializer()
  }
}

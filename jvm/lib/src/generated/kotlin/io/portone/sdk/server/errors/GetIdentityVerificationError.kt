package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetIdentityVerificationErrorSerializer::class)
public sealed interface GetIdentityVerificationError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetIdentityVerificationError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetIdentityVerificationError
}


private object GetIdentityVerificationErrorSerializer : JsonContentPolymorphicSerializer<GetIdentityVerificationError>(GetIdentityVerificationError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "IDENTITY_VERIFICATION_NOT_FOUND" -> IdentityVerificationNotFoundError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetIdentityVerificationError.Unrecognized.serializer()
  }
}

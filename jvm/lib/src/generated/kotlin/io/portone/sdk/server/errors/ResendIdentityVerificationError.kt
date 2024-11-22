package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(ResendIdentityVerificationErrorSerializer::class)
public sealed interface ResendIdentityVerificationError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : ResendIdentityVerificationError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : ResendIdentityVerificationError
}


private object ResendIdentityVerificationErrorSerializer : JsonContentPolymorphicSerializer<ResendIdentityVerificationError>(ResendIdentityVerificationError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "IDENTITY_VERIFICATION_ALREADY_VERIFIED" -> IdentityVerificationAlreadyVerifiedError.serializer()
    "IDENTITY_VERIFICATION_NOT_FOUND" -> IdentityVerificationNotFoundError.serializer()
    "IDENTITY_VERIFICATION_NOT_SENT" -> IdentityVerificationNotSentError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PG_PROVIDER" -> PgProviderError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> ResendIdentityVerificationError.Unrecognized.serializer()
  }
}

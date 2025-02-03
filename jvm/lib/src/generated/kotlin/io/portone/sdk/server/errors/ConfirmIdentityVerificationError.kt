package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(ConfirmIdentityVerificationErrorSerializer::class)
internal sealed interface ConfirmIdentityVerificationError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : ConfirmIdentityVerificationError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : ConfirmIdentityVerificationError
}


private object ConfirmIdentityVerificationErrorSerializer : JsonContentPolymorphicSerializer<ConfirmIdentityVerificationError>(ConfirmIdentityVerificationError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "IDENTITY_VERIFICATION_ALREADY_VERIFIED" -> IdentityVerificationAlreadyVerifiedError.serializer()
    "IDENTITY_VERIFICATION_NOT_FOUND" -> IdentityVerificationNotFoundError.serializer()
    "IDENTITY_VERIFICATION_NOT_SENT" -> IdentityVerificationNotSentError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PG_PROVIDER" -> PgProviderError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> ConfirmIdentityVerificationError.Unrecognized.serializer()
  }
}

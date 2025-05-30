package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(SendIdentityVerificationErrorSerializer::class)
internal sealed interface SendIdentityVerificationError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : SendIdentityVerificationError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : SendIdentityVerificationError
}


private object SendIdentityVerificationErrorSerializer : JsonContentPolymorphicSerializer<SendIdentityVerificationError>(SendIdentityVerificationError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "CHANNEL_NOT_FOUND" -> ChannelNotFoundError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "IDENTITY_VERIFICATION_ALREADY_SENT" -> IdentityVerificationAlreadySentError.serializer()
    "IDENTITY_VERIFICATION_ALREADY_VERIFIED" -> IdentityVerificationAlreadyVerifiedError.serializer()
    "IDENTITY_VERIFICATION_NOT_FOUND" -> IdentityVerificationNotFoundError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "MAX_TRANSACTION_COUNT_REACHED" -> MaxTransactionCountReachedError.serializer()
    "PG_PROVIDER" -> PgProviderError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> SendIdentityVerificationError.Unrecognized.serializer()
  }
}

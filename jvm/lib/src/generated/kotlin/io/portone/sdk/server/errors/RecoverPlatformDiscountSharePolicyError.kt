package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(RecoverPlatformDiscountSharePolicyErrorSerializer::class)
internal sealed interface RecoverPlatformDiscountSharePolicyError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : RecoverPlatformDiscountSharePolicyError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : RecoverPlatformDiscountSharePolicyError
}


private object RecoverPlatformDiscountSharePolicyErrorSerializer : JsonContentPolymorphicSerializer<RecoverPlatformDiscountSharePolicyError>(RecoverPlatformDiscountSharePolicyError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND" -> PlatformDiscountSharePolicyNotFoundError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> RecoverPlatformDiscountSharePolicyError.Unrecognized.serializer()
  }
}

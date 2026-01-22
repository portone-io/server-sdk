package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(DisconnectBulkPartnerMemberCompanyErrorSerializer::class)
internal sealed interface DisconnectBulkPartnerMemberCompanyError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : DisconnectBulkPartnerMemberCompanyError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : DisconnectBulkPartnerMemberCompanyError
}


internal object DisconnectBulkPartnerMemberCompanyErrorSerializer : JsonContentPolymorphicSerializer<DisconnectBulkPartnerMemberCompanyError>(DisconnectBulkPartnerMemberCompanyError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out DisconnectBulkPartnerMemberCompanyError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "PLATFORM_BTX_NOT_ENABLED" -> PlatformBtxNotEnabledError.serializer()
      "PLATFORM_EXTERNAL_API_FAILED" -> PlatformExternalApiFailedError.serializer()
      "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
      "PLATFORM_PARTNER_NOT_FOUND" -> PlatformPartnerNotFoundError.serializer()
      "PLATFORM_TARGET_PARTNER_NOT_FOUND" -> PlatformTargetPartnerNotFoundError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> DisconnectBulkPartnerMemberCompanyError.Unrecognized.serializer()
    }
}

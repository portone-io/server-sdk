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

@Serializable(ConnectPartnerCounterpartyErrorSerializer::class)
internal sealed interface ConnectPartnerCounterpartyError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : ConnectPartnerCounterpartyError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : ConnectPartnerCounterpartyError
}


internal object ConnectPartnerCounterpartyErrorSerializer : JsonContentPolymorphicSerializer<ConnectPartnerCounterpartyError>(ConnectPartnerCounterpartyError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out ConnectPartnerCounterpartyError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "PLATFORM_ARCHIVED_PARTNER" -> PlatformArchivedPartnerError.serializer()
      "PLATFORM_ARCHIVED_PARTNER_NTS_NOT_ALLOWED" -> PlatformArchivedPartnerNtsNotAllowedError.serializer()
      "PLATFORM_BTX_NOT_ENABLED" -> PlatformBtxNotEnabledError.serializer()
      "PLATFORM_COUNTERPARTY_NOT_CONNECTABLE_STATUS" -> PlatformCounterpartyNotConnectableStatusError.serializer()
      "PLATFORM_EXTERNAL_API_FAILED" -> PlatformExternalApiFailedError.serializer()
      "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
      "PLATFORM_PARTNER_NOT_FOUND" -> PlatformPartnerNotFoundError.serializer()
      "PLATFORM_PARTNER_SCHEDULE_EXISTS" -> PlatformPartnerScheduleExistsError.serializer()
      "PLATFORM_PARTNER_TAXATION_TYPE_IS_SIMPLE" -> PlatformPartnerTaxationTypeIsSimpleError.serializer()
      "PLATFORM_PARTNER_TYPE_IS_NOT_BUSINESS" -> PlatformPartnerTypeIsNotBusinessError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> ConnectPartnerCounterpartyError.Unrecognized.serializer()
    }
}

package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(DisconnectPartnerMemberCompanyErrorSerializer::class)
internal sealed interface DisconnectPartnerMemberCompanyError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : DisconnectPartnerMemberCompanyError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : DisconnectPartnerMemberCompanyError
}


private object DisconnectPartnerMemberCompanyErrorSerializer : JsonContentPolymorphicSerializer<DisconnectPartnerMemberCompanyError>(DisconnectPartnerMemberCompanyError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_BTX_NOT_ENABLED" -> PlatformBtxNotEnabledError.serializer()
    "PLATFORM_EXTERNAL_API_FAILED" -> PlatformExternalApiFailedError.serializer()
    "PLATFORM_MEMBER_COMPANY_NOT_CONNECTED" -> PlatformMemberCompanyNotConnectedError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "PLATFORM_ONGOING_TAX_INVOICE_EXISTS" -> PlatformOngoingTaxInvoiceExistsError.serializer()
    "PLATFORM_PARTNER_NOT_FOUND" -> PlatformPartnerNotFoundError.serializer()
    "PLATFORM_PARTNER_TAXATION_TYPE_IS_SIMPLE" -> PlatformPartnerTaxationTypeIsSimpleError.serializer()
    "PLATFORM_PARTNER_TYPE_IS_NOT_BUSINESS" -> PlatformPartnerTypeIsNotBusinessError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> DisconnectPartnerMemberCompanyError.Unrecognized.serializer()
  }
}

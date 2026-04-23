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

@Serializable(CompletePlatformPayoutByPartnerSettlementIdsErrorSerializer::class)
internal sealed interface CompletePlatformPayoutByPartnerSettlementIdsError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : CompletePlatformPayoutByPartnerSettlementIdsError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : CompletePlatformPayoutByPartnerSettlementIdsError
}


internal object CompletePlatformPayoutByPartnerSettlementIdsErrorSerializer : JsonContentPolymorphicSerializer<CompletePlatformPayoutByPartnerSettlementIdsError>(CompletePlatformPayoutByPartnerSettlementIdsError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out CompletePlatformPayoutByPartnerSettlementIdsError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "PLATFORM_BULK_PAYOUT_ID_ALREADY_EXISTS" -> PlatformBulkPayoutIdAlreadyExistsError.serializer()
      "PLATFORM_CURRENCY_NOT_SUPPORTED" -> PlatformNegativePayoutAmountPartnersError.serializer()
      "PLATFORM_DUPLICATED_PARTNER_SETTLEMENT_IDS" -> PlatformDuplicatedPartnerSettlementIdsError.serializer()
      "PLATFORM_NON_PAYABLE_PARTNER_SETTLEMENTS" -> PlatformNonPayablePartnerSettlementsError.serializer()
      "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
      "PLATFORM_NO_SELECTED_PARTNER_SETTLEMENTS" -> PlatformNoSelectedPartnerSettlementsError.serializer()
      "PLATFORM_PARTNER_SETTLEMENTS_NOT_FOUND" -> PlatformPartnerSettlementsNotFoundError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> CompletePlatformPayoutByPartnerSettlementIdsError.Unrecognized.serializer()
    }
}

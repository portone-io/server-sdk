package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CreatePlatformOrderTransferErrorSerializer::class)
internal sealed interface CreatePlatformOrderTransferError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : CreatePlatformOrderTransferError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : CreatePlatformOrderTransferError
}


private object CreatePlatformOrderTransferErrorSerializer : JsonContentPolymorphicSerializer<CreatePlatformOrderTransferError>(CreatePlatformOrderTransferError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_ADDITIONAL_FEE_POLICIES_NOT_FOUND" -> PlatformAdditionalFeePoliciesNotFoundError.serializer()
    "PLATFORM_ADDITIONAL_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED" -> PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError.serializer()
    "PLATFORM_CONTRACT_NOT_FOUND" -> PlatformContractNotFoundError.serializer()
    "PLATFORM_CONTRACT_PLATFORM_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED" -> PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError.serializer()
    "PLATFORM_CURRENCY_NOT_SUPPORTED" -> PlatformCurrencyNotSupportedError.serializer()
    "PLATFORM_DISCOUNT_SHARE_POLICIES_NOT_FOUND" -> PlatformDiscountSharePoliciesNotFoundError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "PLATFORM_PARTNER_NOT_FOUND" -> PlatformPartnerNotFoundError.serializer()
    "PLATFORM_PAYMENT_NOT_FOUND" -> PlatformPaymentNotFoundError.serializer()
    "PLATFORM_PRODUCT_ID_DUPLICATED" -> PlatformProductIdDuplicatedError.serializer()
    "PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED" -> PlatformSettlementAmountExceededError.serializer()
    "PLATFORM_SETTLEMENT_PARAMETER_NOT_FOUND" -> PlatformSettlementParameterNotFoundError.serializer()
    "PLATFORM_SETTLEMENT_PAYMENT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT" -> PlatformSettlementPaymentAmountExceededPortOnePaymentError.serializer()
    "PLATFORM_SETTLEMENT_SUPPLY_WITH_VAT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT" -> PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError.serializer()
    "PLATFORM_SETTLEMENT_TAX_FREE_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT" -> PlatformSettlementTaxFreeAmountExceededPortOnePaymentError.serializer()
    "PLATFORM_TRANSFER_ALREADY_EXISTS" -> PlatformTransferAlreadyExistsError.serializer()
    "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND" -> PlatformUserDefinedPropertyNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CreatePlatformOrderTransferError.Unrecognized.serializer()
  }
}

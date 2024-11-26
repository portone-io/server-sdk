package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CreatePlatformOrderCancelTransferErrorSerializer::class)
public sealed interface CreatePlatformOrderCancelTransferError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : CreatePlatformOrderCancelTransferError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : CreatePlatformOrderCancelTransferError
}


private object CreatePlatformOrderCancelTransferErrorSerializer : JsonContentPolymorphicSerializer<CreatePlatformOrderCancelTransferError>(CreatePlatformOrderCancelTransferError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_CANCELLABLE_AMOUNT_EXCEEDED" -> PlatformCancellableAmountExceededError.serializer()
    "PLATFORM_CANCELLABLE_DISCOUNT_AMOUNT_EXCEEDED" -> PlatformCancellableDiscountAmountExceededError.serializer()
    "PLATFORM_CANCELLABLE_DISCOUNT_TAX_FREE_AMOUNT_EXCEEDED" -> PlatformCancellableDiscountTaxFreeAmountExceededError.serializer()
    "PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED" -> PlatformCancellableProductQuantityExceededError.serializer()
    "PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED" -> PlatformCancellationAndPaymentTypeMismatchedError.serializer()
    "PLATFORM_CANCELLATION_NOT_FOUND" -> PlatformCancellationNotFoundError.serializer()
    "PLATFORM_CANNOT_SPECIFY_TRANSFER" -> PlatformCannotSpecifyTransferError.serializer()
    "PLATFORM_DISCOUNT_SHARE_POLICY_ID_DUPLICATED" -> PlatformDiscountSharePolicyIdDuplicatedError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "PLATFORM_ORDER_DETAIL_MISMATCHED" -> PlatformOrderDetailMismatchedError.serializer()
    "PLATFORM_ORDER_TRANSFER_ALREADY_CANCELLED" -> PlatformOrderTransferAlreadyCancelledError.serializer()
    "PLATFORM_PAYMENT_NOT_FOUND" -> PlatformPaymentNotFoundError.serializer()
    "PLATFORM_PRODUCT_ID_DUPLICATED" -> PlatformProductIdDuplicatedError.serializer()
    "PLATFORM_PRODUCT_ID_NOT_FOUND" -> PlatformProductIdNotFoundError.serializer()
    "PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED" -> PlatformSettlementAmountExceededError.serializer()
    "PLATFORM_SETTLEMENT_CANCEL_AMOUNT_EXCEEDED_PORT_ONE_CANCEL" -> PlatformSettlementCancelAmountExceededPortOneCancelError.serializer()
    "PLATFORM_TRANSFER_ALREADY_EXISTS" -> PlatformTransferAlreadyExistsError.serializer()
    "PLATFORM_TRANSFER_DISCOUNT_SHARE_POLICY_NOT_FOUND" -> PlatformTransferDiscountSharePolicyNotFoundError.serializer()
    "PLATFORM_TRANSFER_NOT_FOUND" -> PlatformTransferNotFoundError.serializer()
    "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND" -> PlatformUserDefinedPropertyNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CreatePlatformOrderCancelTransferError.Unrecognized.serializer()
  }
}

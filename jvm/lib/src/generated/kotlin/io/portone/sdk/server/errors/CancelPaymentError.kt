package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CancelPaymentErrorSerializer::class)
internal sealed interface CancelPaymentError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : CancelPaymentError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : CancelPaymentError
}


private object CancelPaymentErrorSerializer : JsonContentPolymorphicSerializer<CancelPaymentError>(CancelPaymentError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN" -> CancellableAmountConsistencyBrokenError.serializer()
    "CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT" -> CancelAmountExceedsCancellableAmountError.serializer()
    "CANCEL_TAX_AMOUNT_EXCEEDS_CANCELLABLE_TAX_AMOUNT" -> CancelTaxAmountExceedsCancellableTaxAmountError.serializer()
    "CANCEL_TAX_FREE_AMOUNT_EXCEEDS_CANCELLABLE_TAX_FREE_AMOUNT" -> CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "NEGATIVE_PROMOTION_ADJUSTED_CANCEL_AMOUNT" -> NegativePromotionAdjustedCancelAmountError.serializer()
    "PAYMENT_ALREADY_CANCELLED" -> PaymentAlreadyCancelledError.serializer()
    "PAYMENT_NOT_FOUND" -> PaymentNotFoundError.serializer()
    "PAYMENT_NOT_PAID" -> PaymentNotPaidError.serializer()
    "PG_PROVIDER" -> PgProviderError.serializer()
    "PROMOTION_DISCOUNT_RETAIN_OPTION_SHOULD_NOT_BE_CHANGED" -> PromotionDiscountRetainOptionShouldNotBeChangedError.serializer()
    "SUM_OF_PARTS_EXCEEDS_CANCEL_AMOUNT" -> SumOfPartsExceedsCancelAmountError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CancelPaymentError.Unrecognized.serializer()
  }
}

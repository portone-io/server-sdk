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

@Serializable(CancelB2bTaxInvoiceRequestErrorSerializer::class)
internal sealed interface CancelB2bTaxInvoiceRequestError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : CancelB2bTaxInvoiceRequestError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : CancelB2bTaxInvoiceRequestError
}


internal object CancelB2bTaxInvoiceRequestErrorSerializer : JsonContentPolymorphicSerializer<CancelB2bTaxInvoiceRequestError>(CancelB2bTaxInvoiceRequestError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out CancelB2bTaxInvoiceRequestError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "B2B_EXTERNAL_SERVICE" -> B2bExternalServiceError.serializer()
      "B2B_NOT_ENABLED" -> B2bNotEnabledError.serializer()
      "B2B_TAX_INVOICE_NOT_FOUND" -> B2bTaxInvoiceNotFoundError.serializer()
      "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS" -> B2bTaxInvoiceNotRequestedStatusError.serializer()
      "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY" -> B2bTaxInvoiceNoRecipientDocumentKeyError.serializer()
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> CancelB2bTaxInvoiceRequestError.Unrecognized.serializer()
    }
}

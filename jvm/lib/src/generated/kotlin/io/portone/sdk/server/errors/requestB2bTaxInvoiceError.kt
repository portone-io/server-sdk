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

@Serializable(requestB2bTaxInvoiceErrorSerializer::class)
internal sealed interface requestB2bTaxInvoiceError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : requestB2bTaxInvoiceError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : requestB2bTaxInvoiceError
}


internal object requestB2bTaxInvoiceErrorSerializer : JsonContentPolymorphicSerializer<requestB2bTaxInvoiceError>(requestB2bTaxInvoiceError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out requestB2bTaxInvoiceError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "B2B_CANNOT_CHANGE_TAX_TYPE" -> B2BCannotChangeTaxTypeError.serializer()
      "B2B_EXTERNAL_SERVICE" -> B2bExternalServiceError.serializer()
      "B2B_ISSUANCE_TYPE_MISMATCH" -> B2bIssuanceTypeMismatchError.serializer()
      "B2B_MODIFICATION_NOT_PROVIDED" -> B2bModificationNotProvidedError.serializer()
      "B2B_NOT_ENABLED" -> B2bNotEnabledError.serializer()
      "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND" -> B2bOriginalTaxInvoiceNotFoundError.serializer()
      "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS" -> B2bTaxInvoiceNotDraftedStatusError.serializer()
      "B2B_TAX_INVOICE_NOT_FOUND" -> B2bTaxInvoiceNotFoundError.serializer()
      "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY" -> B2bTaxInvoiceNoRecipientDocumentKeyError.serializer()
      "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED" -> B2BTaxInvoiceStatusNotSendingCompletedError.serializer()
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> requestB2bTaxInvoiceError.Unrecognized.serializer()
    }
}

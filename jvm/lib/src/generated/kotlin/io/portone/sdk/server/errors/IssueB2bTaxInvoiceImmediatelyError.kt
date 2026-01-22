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

@Serializable(IssueB2bTaxInvoiceImmediatelyErrorSerializer::class)
internal sealed interface IssueB2bTaxInvoiceImmediatelyError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : IssueB2bTaxInvoiceImmediatelyError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : IssueB2bTaxInvoiceImmediatelyError
}


internal object IssueB2bTaxInvoiceImmediatelyErrorSerializer : JsonContentPolymorphicSerializer<IssueB2bTaxInvoiceImmediatelyError>(IssueB2bTaxInvoiceImmediatelyError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out IssueB2bTaxInvoiceImmediatelyError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "B2B_CANNOT_CHANGE_TAX_TYPE" -> B2BCannotChangeTaxTypeError.serializer()
      "B2B_EXTERNAL_SERVICE" -> B2bExternalServiceError.serializer()
      "B2B_ID_ALREADY_EXISTS" -> B2bIdAlreadyExistsError.serializer()
      "B2B_ISSUANCE_TYPE_MISMATCH" -> B2bIssuanceTypeMismatchError.serializer()
      "B2B_MODIFICATION_NOT_PROVIDED" -> B2bModificationNotProvidedError.serializer()
      "B2B_NOT_ENABLED" -> B2bNotEnabledError.serializer()
      "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND" -> B2bOriginalTaxInvoiceNotFoundError.serializer()
      "B2B_RECIPIENT_NOT_FOUND" -> B2bRecipientNotFoundError.serializer()
      "B2B_SUPPLIER_NOT_FOUND" -> B2bSupplierNotFoundError.serializer()
      "B2B_TAX_INVOICE_NOT_FOUND" -> B2bTaxInvoiceNotFoundError.serializer()
      "B2B_TAX_INVOICE_RECIPIENT_DOCUMENT_KEY_ALREADY_USED" -> B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError.serializer()
      "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED" -> B2BTaxInvoiceStatusNotSendingCompletedError.serializer()
      "B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED" -> B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError.serializer()
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> IssueB2bTaxInvoiceImmediatelyError.Unrecognized.serializer()
    }
}

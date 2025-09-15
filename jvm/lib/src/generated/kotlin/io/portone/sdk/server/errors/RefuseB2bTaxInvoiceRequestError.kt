package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(RefuseB2bTaxInvoiceRequestErrorSerializer::class)
internal sealed interface RefuseB2bTaxInvoiceRequestError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : RefuseB2bTaxInvoiceRequestError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : RefuseB2bTaxInvoiceRequestError
}


private object RefuseB2bTaxInvoiceRequestErrorSerializer : JsonContentPolymorphicSerializer<RefuseB2bTaxInvoiceRequestError>(RefuseB2bTaxInvoiceRequestError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "B2B_EXTERNAL_SERVICE" -> B2bExternalServiceError.serializer()
    "B2B_NOT_ENABLED" -> B2bNotEnabledError.serializer()
    "B2B_TAX_INVOICE_NOT_FOUND" -> B2bTaxInvoiceNotFoundError.serializer()
    "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS" -> B2bTaxInvoiceNotRequestedStatusError.serializer()
    "B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY" -> B2bTaxInvoiceNoSupplierDocumentKeyError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> RefuseB2bTaxInvoiceRequestError.Unrecognized.serializer()
  }
}

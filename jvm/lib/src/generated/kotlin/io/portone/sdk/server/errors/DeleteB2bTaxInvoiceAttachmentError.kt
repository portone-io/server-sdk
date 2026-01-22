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

@Serializable(DeleteB2bTaxInvoiceAttachmentErrorSerializer::class)
internal sealed interface DeleteB2bTaxInvoiceAttachmentError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : DeleteB2bTaxInvoiceAttachmentError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : DeleteB2bTaxInvoiceAttachmentError
}


internal object DeleteB2bTaxInvoiceAttachmentErrorSerializer : JsonContentPolymorphicSerializer<DeleteB2bTaxInvoiceAttachmentError>(DeleteB2bTaxInvoiceAttachmentError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out DeleteB2bTaxInvoiceAttachmentError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "B2B_EXTERNAL_SERVICE" -> B2bExternalServiceError.serializer()
      "B2B_NOT_ENABLED" -> B2bNotEnabledError.serializer()
      "B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND" -> B2bTaxInvoiceAttachmentNotFoundError.serializer()
      "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS" -> B2bTaxInvoiceNotDraftedStatusError.serializer()
      "B2B_TAX_INVOICE_NOT_FOUND" -> B2bTaxInvoiceNotFoundError.serializer()
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> DeleteB2bTaxInvoiceAttachmentError.Unrecognized.serializer()
    }
}

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

@Serializable(DeleteB2bTaxInvoiceErrorSerializer::class)
internal sealed interface DeleteB2bTaxInvoiceError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : DeleteB2bTaxInvoiceError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : DeleteB2bTaxInvoiceError
}


internal object DeleteB2bTaxInvoiceErrorSerializer : JsonContentPolymorphicSerializer<DeleteB2bTaxInvoiceError>(DeleteB2bTaxInvoiceError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out DeleteB2bTaxInvoiceError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "B2B_BULK_TAX_INVOICE_NOT_FOUND" -> B2bBulkTaxInvoiceNotFoundError.serializer()
      "B2B_EXTERNAL_SERVICE" -> B2bExternalServiceError.serializer()
      "B2B_NOT_ENABLED" -> B2bNotEnabledError.serializer()
      "B2B_TAX_INVOICE_NON_DELETABLE_STATUS" -> B2bTaxInvoiceNonDeletableStatusError.serializer()
      "B2B_TAX_INVOICE_NOT_FOUND" -> B2bTaxInvoiceNotFoundError.serializer()
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> DeleteB2bTaxInvoiceError.Unrecognized.serializer()
    }
}

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

@Serializable(GetB2bTaxInvoicePdfDownloadUrlErrorSerializer::class)
internal sealed interface GetB2bTaxInvoicePdfDownloadUrlError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : GetB2bTaxInvoicePdfDownloadUrlError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : GetB2bTaxInvoicePdfDownloadUrlError
}


internal object GetB2bTaxInvoicePdfDownloadUrlErrorSerializer : JsonContentPolymorphicSerializer<GetB2bTaxInvoicePdfDownloadUrlError>(GetB2bTaxInvoicePdfDownloadUrlError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out GetB2bTaxInvoicePdfDownloadUrlError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "B2B_EXTERNAL_SERVICE" -> B2bExternalServiceError.serializer()
      "B2B_NOT_ENABLED" -> B2bNotEnabledError.serializer()
      "B2B_TAX_INVOICE_NOT_FOUND" -> B2bTaxInvoiceNotFoundError.serializer()
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> GetB2bTaxInvoicePdfDownloadUrlError.Unrecognized.serializer()
    }
}

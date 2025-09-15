package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CancelB2bTaxInvoiceIssuanceErrorSerializer::class)
internal sealed interface CancelB2bTaxInvoiceIssuanceError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : CancelB2bTaxInvoiceIssuanceError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : CancelB2bTaxInvoiceIssuanceError
}


private object CancelB2bTaxInvoiceIssuanceErrorSerializer : JsonContentPolymorphicSerializer<CancelB2bTaxInvoiceIssuanceError>(CancelB2bTaxInvoiceIssuanceError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "B2B_EXTERNAL_SERVICE" -> B2bExternalServiceError.serializer()
    "B2B_NOT_ENABLED" -> B2bNotEnabledError.serializer()
    "B2B_TAX_INVOICE_NOT_FOUND" -> B2bTaxInvoiceNotFoundError.serializer()
    "B2B_TAX_INVOICE_NOT_ISSUED_STATUS" -> B2bTaxInvoiceNotIssuedStatusError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CancelB2bTaxInvoiceIssuanceError.Unrecognized.serializer()
  }
}

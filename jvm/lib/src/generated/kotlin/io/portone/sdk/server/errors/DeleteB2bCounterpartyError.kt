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

@Serializable(DeleteB2bCounterpartyErrorSerializer::class)
internal sealed interface DeleteB2bCounterpartyError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : DeleteB2bCounterpartyError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : DeleteB2bCounterpartyError
}


internal object DeleteB2bCounterpartyErrorSerializer : JsonContentPolymorphicSerializer<DeleteB2bCounterpartyError>(DeleteB2bCounterpartyError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out DeleteB2bCounterpartyError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "B2B_COUNTERPARTY_NOT_FOUND" -> B2bCounterpartyNotFoundError.serializer()
      "B2B_COUNTERPARTY_ONGOING_TAX_INVOICE_EXISTS" -> B2bCounterpartyOngoingTaxInvoiceExistsError.serializer()
      "B2B_COUNTERPARTY_PARTNER_NOT_DELETABLE" -> B2bCounterpartyPartnerNotDeletableError.serializer()
      "B2B_EXTERNAL_SERVICE" -> B2bExternalServiceError.serializer()
      "B2B_NOT_ENABLED" -> B2bNotEnabledError.serializer()
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> DeleteB2bCounterpartyError.Unrecognized.serializer()
    }
}

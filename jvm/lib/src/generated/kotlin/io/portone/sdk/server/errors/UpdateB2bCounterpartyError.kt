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

@Serializable(UpdateB2bCounterpartyErrorSerializer::class)
internal sealed interface UpdateB2bCounterpartyError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : UpdateB2bCounterpartyError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : UpdateB2bCounterpartyError
}


internal object UpdateB2bCounterpartyErrorSerializer : JsonContentPolymorphicSerializer<UpdateB2bCounterpartyError>(UpdateB2bCounterpartyError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out UpdateB2bCounterpartyError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "B2B_COUNTERPARTY_BRN_MODIFICATION_NOT_ALLOWED" -> B2bCounterpartyBrnModificationNotAllowedError.serializer()
      "B2B_COUNTERPARTY_MISSING_REQUIRED_FIELDS" -> B2bCounterpartyMissingRequiredFieldsError.serializer()
      "B2B_COUNTERPARTY_NOT_FOUND" -> B2bCounterpartyNotFoundError.serializer()
      "B2B_COUNTERPARTY_PARTNER_NOT_UPDATABLE" -> B2bCounterpartyPartnerNotUpdatableError.serializer()
      "B2B_COUNTERPARTY_TOO_MANY_ADDITIONAL_CONTACTS" -> B2bCounterpartyTooManyAdditionalContactsError.serializer()
      "B2B_COUNTERPARTY_VERIFICATION_BRN_MISMATCH" -> B2bCounterpartyVerificationBrnMismatchError.serializer()
      "B2B_COUNTERPARTY_VERIFICATION_INVALID" -> B2bCounterpartyVerificationInvalidError.serializer()
      "B2B_COUNTERPARTY_VERIFICATION_NOT_FOUND" -> B2bCounterpartyVerificationNotFoundError.serializer()
      "B2B_COUNTERPARTY_VERIFICATION_TYPE_MISMATCH" -> B2bCounterpartyVerificationTypeMismatchError.serializer()
      "B2B_EXTERNAL_SERVICE" -> B2bExternalServiceError.serializer()
      "B2B_NOT_ENABLED" -> B2bNotEnabledError.serializer()
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> UpdateB2bCounterpartyError.Unrecognized.serializer()
    }
}

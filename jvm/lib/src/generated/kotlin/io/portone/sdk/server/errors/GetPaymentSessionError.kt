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

@Serializable(GetPaymentSessionErrorSerializer::class)
internal sealed interface GetPaymentSessionError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : GetPaymentSessionError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : GetPaymentSessionError
}


internal object GetPaymentSessionErrorSerializer : JsonContentPolymorphicSerializer<GetPaymentSessionError>(GetPaymentSessionError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out GetPaymentSessionError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "SESSION_EXPIRED" -> SessionExpiredError.serializer()
      "SESSION_NOT_FOUND" -> SessionNotFoundError.serializer()
      else -> GetPaymentSessionError.Unrecognized.serializer()
    }
}

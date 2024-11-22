package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(ModifyEscrowLogisticsErrorSerializer::class)
public sealed interface ModifyEscrowLogisticsError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : ModifyEscrowLogisticsError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : ModifyEscrowLogisticsError
}


private object ModifyEscrowLogisticsErrorSerializer : JsonContentPolymorphicSerializer<ModifyEscrowLogisticsError>(ModifyEscrowLogisticsError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PAYMENT_NOT_FOUND" -> PaymentNotFoundError.serializer()
    "PAYMENT_NOT_PAID" -> PaymentNotPaidError.serializer()
    "PG_PROVIDER" -> PgProviderError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> ModifyEscrowLogisticsError.Unrecognized.serializer()
  }
}

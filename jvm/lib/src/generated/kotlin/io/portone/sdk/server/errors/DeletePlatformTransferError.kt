package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(DeletePlatformTransferErrorSerializer::class)
public sealed interface DeletePlatformTransferError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : DeletePlatformTransferError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : DeletePlatformTransferError
}


private object DeletePlatformTransferErrorSerializer : JsonContentPolymorphicSerializer<DeletePlatformTransferError>(DeletePlatformTransferError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_CANCEL_ORDER_TRANSFERS_EXISTS" -> PlatformCancelOrderTransfersExistsError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "PLATFORM_TRANSFER_NON_DELETABLE_STATUS" -> PlatformTransferNonDeletableStatusError.serializer()
    "PLATFORM_TRANSFER_NOT_FOUND" -> PlatformTransferNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> DeletePlatformTransferError.Unrecognized.serializer()
  }
}

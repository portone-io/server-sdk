package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(DownloadPlatformTransferSheetErrorSerializer::class)
public sealed interface DownloadPlatformTransferSheetError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : DownloadPlatformTransferSheetError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : DownloadPlatformTransferSheetError
}


private object DownloadPlatformTransferSheetErrorSerializer : JsonContentPolymorphicSerializer<DownloadPlatformTransferSheetError>(DownloadPlatformTransferSheetError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> DownloadPlatformTransferSheetError.Unrecognized.serializer()
  }
}

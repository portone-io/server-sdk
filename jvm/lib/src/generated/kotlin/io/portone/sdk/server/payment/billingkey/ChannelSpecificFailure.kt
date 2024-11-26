package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.SelectedChannel
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(ChannelSpecificFailureSerializer::class)
public sealed interface ChannelSpecificFailure {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : ChannelSpecificFailure {
    public val channel: SelectedChannel
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : ChannelSpecificFailure
}


private object ChannelSpecificFailureSerializer : JsonContentPolymorphicSerializer<ChannelSpecificFailure>(ChannelSpecificFailure::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "INVALID_REQUEST" -> ChannelSpecificFailureInvalidRequest.serializer()
    "PG_PROVIDER" -> ChannelSpecificFailurePgProvider.serializer()
    else -> ChannelSpecificFailure.Unrecognized.serializer()
  }
}

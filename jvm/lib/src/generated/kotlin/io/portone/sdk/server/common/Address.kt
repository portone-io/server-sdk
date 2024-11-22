package io.portone.sdk.server.common

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/**
 * 분리 형식 주소
 *
 * oneLine(한 줄 형식 주소) 필드는 항상 존재합니다.
 */
@Serializable(AddressSerializer::class)
public sealed interface Address {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : Address {
    /** 주소 (한 줄) */
    public val oneLine: String
  }
  @Serializable
  public data object Unrecognized : Address
}


private object AddressSerializer : JsonContentPolymorphicSerializer<Address>(Address::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "ONE_LINE" -> OneLineAddress.serializer()
    "SEPARATED" -> SeparatedAddress.serializer()
    else -> Address.Unrecognized.serializer()
  }
}

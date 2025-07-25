package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KeepGeneratedSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.JsonObject
import kotlinx.serialization.json.JsonTransformingSerializer
import kotlinx.serialization.json.jsonObject

@Serializable(TransferParametersSerializer::class)
@KeepGeneratedSerializer
public data class TransferParameters(
  val additionalProperties: Map<String, PlatformSettlementParameterValue>,
)


private class TransferParametersSerializer : JsonTransformingSerializer<TransferParameters>(TransferParameters.generatedSerializer()) {
  companion object {
    private val KNOWN_KEYS = setOf<String>()
  }
  override fun transformSerialize(element: JsonElement): JsonElement = if (element is JsonObject)
    JsonObject(buildMap {
      putAll(element.filterKeys { it != "additionalProperties" })
      putAll(element.getValue("additionalProperties").jsonObject)
    })
  else element
  override fun transformDeserialize(element: JsonElement): JsonElement = if (element is JsonObject)
    JsonObject(buildMap {
      val additionalProperties = mutableMapOf<String, JsonElement>()
      element.forEach { key, value ->
        if (KNOWN_KEYS.contains(key)) put(key, value) else additionalProperties.put(key, value)
      }
      put("additionalProperties", JsonObject(additionalProperties))
    })
  else element
}

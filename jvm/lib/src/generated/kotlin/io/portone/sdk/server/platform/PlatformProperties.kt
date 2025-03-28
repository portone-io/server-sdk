package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.KeepGeneratedSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.buildClassSerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.JsonObject
import kotlinx.serialization.json.JsonTransformingSerializer
import kotlinx.serialization.json.encodeToJsonElement
import kotlinx.serialization.json.jsonObject

@Serializable(PlatformPropertiesSerializer::class)
@KeepGeneratedSerializer
public data object PlatformProperties

// ✅ generatedSerializer() 없이 작동하도록 serializer 직접 구현
private object PlatformPropertiesInnerSerializer : KSerializer<PlatformProperties> {
    override val descriptor = buildClassSerialDescriptor("PlatformProperties") {}

    override fun serialize(encoder: Encoder, value: PlatformProperties) {
        // serialize as empty JSON object
        val json = JsonObject(emptyMap())
        encoder.encodeSerializableValue(JsonObject.serializer(), json)
    }

    override fun deserialize(decoder: Decoder): PlatformProperties {
        decoder.decodeSerializableValue(JsonObject.serializer()) // discard content
        return PlatformProperties
    }
}

// ✅ transform 로직은 그대로 유지
private class PlatformPropertiesSerializer :
    JsonTransformingSerializer<PlatformProperties>(PlatformPropertiesInnerSerializer) {

    companion object {
        private val KNOWN_KEYS = setOf<String>() // 확장 가능
    }

    override fun transformSerialize(element: JsonElement): JsonElement =
        if (element is JsonObject)
            JsonObject(buildMap {
                putAll(element.filterKeys { it != "additionalProperties" })
                putAll(element["additionalProperties"]?.jsonObject ?: emptyMap())
            })
        else element

    override fun transformDeserialize(element: JsonElement): JsonElement =
        if (element is JsonObject)
            JsonObject(buildMap {
                val additionalProperties = mutableMapOf<String, JsonElement>()
                element.forEach { key, value ->
                    if (KNOWN_KEYS.contains(key)) {
                        put(key, value)
                    } else {
                        additionalProperties[key] = value
                    }
                }
                put("additionalProperties", JsonObject(additionalProperties))
            })
        else element
}
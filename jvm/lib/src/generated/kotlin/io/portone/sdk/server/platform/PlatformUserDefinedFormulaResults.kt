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
import kotlinx.serialization.json.jsonObject

@Serializable(PlatformUserDefinedFormulaResultsSerializer::class)
@KeepGeneratedSerializer
public data object PlatformUserDefinedFormulaResults

// ✅ generatedSerializer() 대신 직접 serializer 구현
private object PlatformUserDefinedFormulaResultsInnerSerializer : KSerializer<PlatformUserDefinedFormulaResults> {
    override val descriptor = buildClassSerialDescriptor("PlatformUserDefinedFormulaResults") {}

    override fun serialize(encoder: Encoder, value: PlatformUserDefinedFormulaResults) {
        encoder.encodeSerializableValue(JsonObject.serializer(), JsonObject(emptyMap()))
    }

    override fun deserialize(decoder: Decoder): PlatformUserDefinedFormulaResults {
        decoder.decodeSerializableValue(JsonObject.serializer()) // 무시
        return PlatformUserDefinedFormulaResults
    }
}

// ✅ 기존 transform 로직은 그대로 유지
private class PlatformUserDefinedFormulaResultsSerializer :
    JsonTransformingSerializer<PlatformUserDefinedFormulaResults>(PlatformUserDefinedFormulaResultsInnerSerializer) {

    companion object {
        private val KNOWN_KEYS = setOf<String>() // 필요시 확장
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
                    if (KNOWN_KEYS.contains(key)) put(key, value)
                    else additionalProperties[key] = value
                }
                put("additionalProperties", JsonObject(additionalProperties))
            })
        else element
}
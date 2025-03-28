package io.portone.sdk.server.platform.transfer

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

@Serializable(TransferParametersSerializer::class)
@KeepGeneratedSerializer
public data object TransferParameters

// ✅ generatedSerializer 없이 직접 구현
private object TransferParametersInnerSerializer : KSerializer<TransferParameters> {
    override val descriptor = buildClassSerialDescriptor("TransferParameters") {}

    override fun serialize(encoder: Encoder, value: TransferParameters) {
        encoder.encodeSerializableValue(JsonObject.serializer(), JsonObject(emptyMap()))
    }

    override fun deserialize(decoder: Decoder): TransferParameters {
        decoder.decodeSerializableValue(JsonObject.serializer()) // 내용 무시
        return TransferParameters
    }
}

// ✅ transform 로직 유지
private class TransferParametersSerializer :
    JsonTransformingSerializer<TransferParameters>(TransferParametersInnerSerializer) {

    companion object {
        private val KNOWN_KEYS = setOf<String>()
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
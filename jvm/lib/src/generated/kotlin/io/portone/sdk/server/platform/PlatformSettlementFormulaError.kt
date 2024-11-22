package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(PlatformSettlementFormulaErrorSerializer::class)
public sealed interface PlatformSettlementFormulaError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : PlatformSettlementFormulaError {
  }
  @Serializable
  public data object Unrecognized : PlatformSettlementFormulaError
}


private object PlatformSettlementFormulaErrorSerializer : JsonContentPolymorphicSerializer<PlatformSettlementFormulaError>(PlatformSettlementFormulaError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "INVALID_FUNCTION" -> PlatformSettlementFormulaInvalidFunction.serializer()
    "INVALID_OPERATOR" -> PlatformSettlementFormulaInvalidOperator.serializer()
    "INVALID_SYNTAX" -> PlatformSettlementFormulaInvalidSyntax.serializer()
    "INVALID_VARIABLE" -> PlatformSettlementFormulaInvalidVariable.serializer()
    "UNEXPECTED_FUNCTION_ARGUMENTS" -> PlatformSettlementFormulaUnexpectedFunctionArguments.serializer()
    "UNKNOWN_ERROR" -> PlatformSettlementFormulaUnknownError.serializer()
    "UNSUPPORTED_VARIABLE" -> PlatformSettlementFormulaUnsupportedVariable.serializer()
    else -> PlatformSettlementFormulaError.Unrecognized.serializer()
  }
}

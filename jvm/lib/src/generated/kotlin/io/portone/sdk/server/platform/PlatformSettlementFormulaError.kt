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
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PlatformSettlementFormulaError {
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
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

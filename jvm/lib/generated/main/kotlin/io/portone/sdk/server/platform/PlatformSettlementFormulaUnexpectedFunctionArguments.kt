package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformSettlementFormulaPosition
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("UNEXPECTED_FUNCTION_ARGUMENTS")
public data class PlatformSettlementFormulaUnexpectedFunctionArguments(
  val functionName: String,
  val expectedCount: Int,
  val currentCount: Int,
  val position: PlatformSettlementFormulaPosition,
): PlatformSettlementFormulaError,

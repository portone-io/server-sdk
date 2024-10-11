package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformSettlementFormulaError
import io.portone.sdk.server.platform.PlatformSettlementFormulaPosition
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("INVALID_OPERATOR")
public data class PlatformSettlementFormulaInvalidOperator(
  val `operator`: String,
  val position: PlatformSettlementFormulaPosition,
): PlatformSettlementFormulaError

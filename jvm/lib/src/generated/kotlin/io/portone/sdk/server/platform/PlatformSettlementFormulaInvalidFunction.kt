package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformSettlementFormulaPosition
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("INVALID_FUNCTION")
public data class PlatformSettlementFormulaInvalidFunction(
  val name: String,
  val position: PlatformSettlementFormulaPosition,
) : PlatformSettlementFormulaError

package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformSettlementFormulaPosition
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("INVALID_VARIABLE")
public data class PlatformSettlementFormulaInvalidVariable(
  val name: String,
  val position: PlatformSettlementFormulaPosition,
) : PlatformSettlementFormulaError.Recognized



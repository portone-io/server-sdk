package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformSettlementFormulaPosition
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("UNSUPPORTED_VARIABLE")
public data class PlatformSettlementFormulaUnsupportedVariable(
  val name: String,
  val position: PlatformSettlementFormulaPosition,
) : PlatformSettlementFormulaError

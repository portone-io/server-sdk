package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformSettlementFormulaPosition
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("INVALID_SYNTAX")
public data class PlatformSettlementFormulaInvalidSyntax(
  val syntax: String,
  val position: PlatformSettlementFormulaPosition,
) : PlatformSettlementFormulaError

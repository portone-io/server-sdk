package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

@Serializable
public data class PlatformSettlementFormulaPosition(
  val startLine: Int,
  val startIndex: Int,
  val endLine: Int,
  val endIndex: Int,
)

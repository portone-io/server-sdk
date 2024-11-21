package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformSettlementFormulaError {
  public sealed interface Recognized : PlatformSettlementFormulaError {
  }
  public data object Unrecognized : PlatformSettlementFormulaError
}

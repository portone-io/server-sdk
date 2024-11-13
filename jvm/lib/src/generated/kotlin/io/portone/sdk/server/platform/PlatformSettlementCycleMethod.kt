package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 플랫폼 정산 주기 계산 방식 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformSettlementCycleMethod {
  public data object Unrecognized : PlatformSettlementCycleMethod
}

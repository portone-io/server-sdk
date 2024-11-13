package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 매일 정산 */
@Serializable
@SerialName("DAILY")
public data object PlatformSettlementCycleMethodDaily : PlatformSettlementCycleMethod

package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("UNKNOWN_ERROR")
public data object PlatformSettlementFormulaUnknownError : PlatformSettlementFormulaError.Recognized

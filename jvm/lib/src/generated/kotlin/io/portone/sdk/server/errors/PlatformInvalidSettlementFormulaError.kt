package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.UpdatePlatformError
import io.portone.sdk.server.platform.PlatformSettlementFormulaError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_INVALID_SETTLEMENT_FORMULA")
@ConsistentCopyVisibility
public data class PlatformInvalidSettlementFormulaError internal constructor(
  val platformFee: PlatformSettlementFormulaError? = null,
  val discountShare: PlatformSettlementFormulaError? = null,
  val additionalFee: PlatformSettlementFormulaError? = null,
  override val message: String? = null,
): UpdatePlatformError
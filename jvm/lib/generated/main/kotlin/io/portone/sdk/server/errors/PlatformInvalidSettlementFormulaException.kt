package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.PlatformInvalidSettlementFormulaError
import io.portone.sdk.server.platform.PlatformSettlementFormulaError
import java.lang.Exception


public class PlatformInvalidSettlementFormulaException(
  cause: PlatformInvalidSettlementFormulaError
) : Exception(cause.message) {
  public val platformFee: PlatformSettlementFormulaError? = cause.platformFee,
  public val discountShare: PlatformSettlementFormulaError? = cause.discountShare,
  public val additionalFee: PlatformSettlementFormulaError? = cause.additionalFee,
}

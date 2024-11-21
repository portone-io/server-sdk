package io.portone.sdk.server.errors

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.errors.PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
import java.lang.Exception
import kotlin.String


public class PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedException internal constructor(
  cause: PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
) : PortOneException(cause.message), CreatePlatformOrderTransferException {
  public val id: String = cause.id
  public val graphqlId: String = cause.graphqlId
  public val feeCurrency: Currency = cause.feeCurrency
  public val settlementCurrency: Currency = cause.settlementCurrency
}

package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_ADDITIONAL_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED")
public data class PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError(
  val id: String,
  val graphqlId: String,
  val feeCurrency: Currency,
  val settlementCurrency: Currency,
  override val message: String? = null,
): CreatePlatformOrderTransferError,

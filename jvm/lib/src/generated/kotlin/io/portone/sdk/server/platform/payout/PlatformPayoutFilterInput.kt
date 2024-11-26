package io.portone.sdk.server.platform.payout

import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.payout.PlatformPayoutFilterInputCriteria
import io.portone.sdk.server.platform.payout.PlatformPayoutStatus
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformPayoutFilterInput(
  val statuses: List<PlatformPayoutStatus>? = null,
  val partnerIds: List<String>? = null,
  val criteria: PlatformPayoutFilterInputCriteria,
  /** 은행 */
  val payoutAccountBanks: List<Bank>? = null,
  val partnerTags: List<String>? = null,
  /** 통화 단위 */
  val payoutCurrencies: List<Currency>? = null,
)



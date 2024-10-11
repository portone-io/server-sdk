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
  val criteria: PlatformPayoutFilterInputCriteria,
  val statuses: Array<PlatformPayoutStatus>? = null,
  val partnerIds: Array<String>? = null,
  /** 은행 */
  val payoutAccountBanks: Array<Bank>? = null,
  val partnerTags: Array<String>? = null,
  /** 통화 단위 */
  val payoutCurrencies: Array<Currency>? = null,
)

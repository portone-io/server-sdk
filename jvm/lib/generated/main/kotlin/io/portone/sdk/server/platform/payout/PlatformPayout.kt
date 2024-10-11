package io.portone.sdk.server.platform.payout

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.PlatformPayoutMethod
import io.portone.sdk.server.platform.payout.PlatformPayoutAccount
import io.portone.sdk.server.platform.payout.PlatformPayoutStatus
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformPayout(
  /** 지급 고유 아이디 */
  val id: String,
  val graphqlId: String,
  val method: PlatformPayoutMethod,
  val status: PlatformPayoutStatus,
  val statusUpdatedAt: Instant,
  val partner: PlatformPartner,
  val account: PlatformPayoutAccount,
  val currency: Currency,
  val amount: Long,
  val settlementAmount: Long,
  val incomeTaxAmount: Long,
  val localIncomeTaxAmount: Long,
  val createdAt: Instant,
  val memo: String? = null,
  val withdrawalMemo: String? = null,
  val depositMemo: String? = null,
)

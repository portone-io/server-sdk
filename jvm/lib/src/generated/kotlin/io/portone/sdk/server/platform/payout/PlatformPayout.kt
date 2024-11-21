package io.portone.sdk.server.platform.payout

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.PlatformPayoutMethod
import io.portone.sdk.server.platform.payout.PlatformPayoutAccount
import io.portone.sdk.server.platform.payout.PlatformPayoutStatus
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformPayout(
  /** 지급 고유 아이디 */
  val id: String,
  val graphqlId: String,
  val method: PlatformPayoutMethod,
  val status: PlatformPayoutStatus,
  val statusUpdatedAt: @Serializable(InstantSerializer::class) Instant,
  val memo: String? = null,
  val partner: PlatformPartner,
  val account: PlatformPayoutAccount,
  val currency: Currency,
  val amount: Long,
  val settlementAmount: Long,
  val incomeTaxAmount: Long,
  val localIncomeTaxAmount: Long,
  val withdrawalMemo: String? = null,
  val depositMemo: String? = null,
  val createdAt: @Serializable(InstantSerializer::class) Instant,
  val scheduledAt: @Serializable(InstantSerializer::class) Instant? = null,
)

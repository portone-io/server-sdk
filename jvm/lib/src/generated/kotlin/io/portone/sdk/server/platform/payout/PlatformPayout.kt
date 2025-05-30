package io.portone.sdk.server.platform.payout

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.PlatformPayoutMethod
import io.portone.sdk.server.platform.SettlementAmountType
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
  /** 지급금액 */
  val amount: Long,
  /** 공급가액 */
  val supplyAmount: Long,
  /** 면세 금액 */
  val taxFreeAmount: Long,
  /** 부가세 */
  val vatAmount: Long,
  /** 정산 금액 */
  val settlementAmount: Long,
  /** 정산 면세 금액 */
  val settlementTaxFreeAmount: Long,
  /** 원천징수세액 (소득세) */
  val incomeTaxAmount: Long,
  /** 원천징수세액 (지방소득세) */
  val localIncomeTaxAmount: Long,
  val withdrawalMemo: String? = null,
  val depositMemo: String? = null,
  val createdAt: @Serializable(InstantSerializer::class) Instant,
  val scheduledAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 실패 사유 */
  val failReason: String? = null,
  /** 지급 금액에서 원천징수세 차감 여부 */
  val deductWht: Boolean,
  /** 정산 금액 취급 기준 */
  val settlementAmountType: SettlementAmountType,
)



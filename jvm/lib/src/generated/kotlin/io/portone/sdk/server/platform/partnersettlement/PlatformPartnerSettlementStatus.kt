package io.portone.sdk.server.platform.partnersettlement

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 상태 */
@Serializable
public sealed interface PlatformPartnerSettlementStatus {
  public val value: String
  /** 지급 예약 */
  @SerialName("PAYOUT_SCHEDULED")
  public data object PayoutScheduled : PlatformPartnerSettlementStatus {
    override val value: String = "PAYOUT_SCHEDULED"
  }
  /** 지급 예정 */
  @SerialName("PAYOUT_PREPARED")
  public data object PayoutPrepared : PlatformPartnerSettlementStatus {
    override val value: String = "PAYOUT_PREPARED"
  }
  /** 지급 보류 */
  @SerialName("PAYOUT_WITHHELD")
  public data object PayoutWithheld : PlatformPartnerSettlementStatus {
    override val value: String = "PAYOUT_WITHHELD"
  }
  /** 지급 실패 */
  @SerialName("PAYOUT_FAILED")
  public data object PayoutFailed : PlatformPartnerSettlementStatus {
    override val value: String = "PAYOUT_FAILED"
  }
  /** 지급 중 */
  @SerialName("IN_PAYOUT")
  public data object InPayout : PlatformPartnerSettlementStatus {
    override val value: String = "IN_PAYOUT"
  }
  /** 지급 완료 */
  @SerialName("PAID_OUT")
  public data object PaidOut : PlatformPartnerSettlementStatus {
    override val value: String = "PAID_OUT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerSettlementStatus
}

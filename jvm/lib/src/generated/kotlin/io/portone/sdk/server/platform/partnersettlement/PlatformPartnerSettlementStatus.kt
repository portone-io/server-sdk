package io.portone.sdk.server.platform.partnersettlement

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 상태 */
@Serializable
public sealed class PlatformPartnerSettlementStatus {
  /** 지급 예약 */
  @SerialName("PAYOUT_SCHEDULED")
  public data object PayoutScheduled : PlatformPartnerSettlementStatus()
  /** 지급 예정 */
  @SerialName("PAYOUT_PREPARED")
  public data object PayoutPrepared : PlatformPartnerSettlementStatus()
  /** 지급 보류 */
  @SerialName("PAYOUT_WITHHELD")
  public data object PayoutWithheld : PlatformPartnerSettlementStatus()
  /** 지급 실패 */
  @SerialName("PAYOUT_FAILED")
  public data object PayoutFailed : PlatformPartnerSettlementStatus()
  /** 지급 중 */
  @SerialName("IN_PAYOUT")
  public data object InPayout : PlatformPartnerSettlementStatus()
  /** 지급 완료 */
  @SerialName("PAID_OUT")
  public data object PaidOut : PlatformPartnerSettlementStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformPartnerSettlementStatus()
}

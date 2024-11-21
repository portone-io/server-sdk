package io.portone.sdk.server.platform.policy

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 정산 주기 계산 방식 */
@Serializable
public sealed interface PlatformSettlementCycleType {
  public val value: String
  /** 매일 정산 */
  @SerialName("DAILY")
  public data object Daily : PlatformSettlementCycleType {
    override val value: String = "DAILY"
  }
  /** 매주 정해진 요일에 정산 */
  @SerialName("WEEKLY")
  public data object Weekly : PlatformSettlementCycleType {
    override val value: String = "WEEKLY"
  }
  /** 매월 정해진 날(일)에 정산 */
  @SerialName("MONTHLY")
  public data object Monthly : PlatformSettlementCycleType {
    override val value: String = "MONTHLY"
  }
  /** 정해진 날짜(월, 일)에 정산 */
  @SerialName("MANUAL_DATES")
  public data object ManualDates : PlatformSettlementCycleType {
    override val value: String = "MANUAL_DATES"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformSettlementCycleType
}

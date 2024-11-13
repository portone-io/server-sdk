package io.portone.sdk.server.platform.policy

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 정산 주기 계산 방식 */
@Serializable
public sealed class PlatformSettlementCycleType {
  /** 매일 정산 */
  @SerialName("DAILY")
  public data object Daily : PlatformSettlementCycleType()
  /** 매주 정해진 요일에 정산 */
  @SerialName("WEEKLY")
  public data object Weekly : PlatformSettlementCycleType()
  /** 매월 정해진 날(일)에 정산 */
  @SerialName("MONTHLY")
  public data object Monthly : PlatformSettlementCycleType()
  /** 정해진 날짜(월, 일)에 정산 */
  @SerialName("MANUAL_DATES")
  public data object ManualDates : PlatformSettlementCycleType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformSettlementCycleType()
}

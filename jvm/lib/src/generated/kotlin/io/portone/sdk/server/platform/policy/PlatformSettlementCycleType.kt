package io.portone.sdk.server.platform.policy

import kotlinx.serialization.Serializable

/** 플랫폼 정산 주기 계산 방식 */
@Serializable
public enum class PlatformSettlementCycleType {
  /** 매일 정산 */
  Daily,
  /** 매주 정해진 요일에 정산 */
  Weekly,
  /** 매월 정해진 날(일)에 정산 */
  Monthly,
  /** 정해진 날짜(월, 일)에 정산 */
  ManualDates,
}

package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformSettlementCycleMethodDailyInput
import io.portone.sdk.server.platform.PlatformSettlementCycleMethodManualDatesInput
import io.portone.sdk.server.platform.PlatformSettlementCycleMethodMonthlyInput
import io.portone.sdk.server.platform.PlatformSettlementCycleMethodWeeklyInput
import kotlinx.serialization.Serializable

/**
 * 플랫폼 정산 주기 계산 방식 입력 정보
 *
 * 하나의 하위 필드에만 값을 명시하여 요청합니다.
 */
@Serializable
public data class PlatformSettlementCycleMethodInput(
  /** 매일 정산 */
  val daily: PlatformSettlementCycleMethodDailyInput? = null,
  /** 매주 정해진 요일에 정산 */
  val weekly: PlatformSettlementCycleMethodWeeklyInput? = null,
  /** 매월 정해진 날(일)에 정산 */
  val monthly: PlatformSettlementCycleMethodMonthlyInput? = null,
  /** 정해진 날짜(월, 일)에 정산 */
  val manualDates: PlatformSettlementCycleMethodManualDatesInput? = null,
)

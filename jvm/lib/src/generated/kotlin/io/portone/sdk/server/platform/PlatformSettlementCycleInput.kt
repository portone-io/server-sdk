package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformSettlementCycleDatePolicy
import io.portone.sdk.server.platform.PlatformSettlementCycleMethodInput
import kotlinx.serialization.Serializable

/** 플랫폼 정산 주기 입력 정보 */
@Serializable
public data class PlatformSettlementCycleInput(
  /**
   * 지체일 (d+n 의 n)
   *
   * 정산시작일(통상 주문완료일)로부터 더해진 다음 날짜로부터 가장 가까운 날에 정산이 됩니다. 최소 1 에서 최대 10 까지 지정할 수 있습니다.
   */
  val lagDays: Int,
  /** 기준일로, 정산일 계산 시 공휴일을 고려하기 위한 정보입니다. */
  val datePolicy: PlatformSettlementCycleDatePolicy,
  /** 정산 주기 계산 방식 */
  val method: PlatformSettlementCycleMethodInput,
)

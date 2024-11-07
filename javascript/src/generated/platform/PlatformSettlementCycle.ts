import type { PlatformSettlementCycleDatePolicy } from "./../platform/PlatformSettlementCycleDatePolicy"
import type { PlatformSettlementCycleMethod } from "./../platform/PlatformSettlementCycleMethod"

/**
 * 정산 주기
 *
 * 지체일, 정산일, 기준일로 구성되며, 해당 요소들의 조합으로 실제 정산일을 계산합니다.
 */
export type PlatformSettlementCycle = {
	/**
	 * 지체일 (d+n 의 n)
	 *
	 * 정산시작일(통상 주문완료일)로부터 더해진 다음 날짜로부터 가장 가까운 날에 정산이 됩니다. 최소 1 에서 최대 10 까지 지정할 수 있습니다.
	 * (int32)
	 */
	lagDays: number
	/** 기준일로, 정산일 계산 시 공휴일을 고려하기 위한 정보입니다. */
	datePolicy: PlatformSettlementCycleDatePolicy
	/** 정산 주기 계산 방식 */
	method: PlatformSettlementCycleMethod
}

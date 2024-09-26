import type { PlatformContractFilterInputKeyword } from "#generated/platform/policy/PlatformContractFilterInputKeyword"
import type { PlatformPayer } from "#generated/platform/PlatformPayer"
import type { PlatformSettlementCycleDatePolicy } from "#generated/platform/PlatformSettlementCycleDatePolicy"
import type { PlatformSettlementCycleType } from "#generated/platform/policy/PlatformSettlementCycleType"

/** 계약 다건 조회를 위한 필터 조건 */
export type PlatformContractFilterInput = {
	/**
	 * 금액 부담 주체
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 수수료 부담 주체를 가진 계약만 조회합니다.
	 */
	platformFeePayers?: PlatformPayer[]
	/**
	 * 플랫폼 정산 주기 계산 방식
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 정산 주기 계산 방식을 가진 계약만 조회합니다.
	 */
	cycleTypes?: PlatformSettlementCycleType[]
	/**
	 * 플랫폼 정산 기준일
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 정산 기준일을 가진 계약만 조회합니다.
	 */
	datePolicies?: PlatformSettlementCycleDatePolicy[]
	/**
	 * 보관 조회 여부
	 *
	 * true 이면 보관된 계약을 조회하고, false 이면 보관되지 않은 계약을 조회합니다. 기본값은 false 입니다.
	 */
	isArchived?: boolean
	/** 검색 키워드 */
	keyword?: PlatformContractFilterInputKeyword
}

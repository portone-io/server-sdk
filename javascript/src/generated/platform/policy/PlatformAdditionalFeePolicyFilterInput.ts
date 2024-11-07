import type { PlatformAdditionalFeePolicyFilterInputKeyword } from "./../../platform/policy/PlatformAdditionalFeePolicyFilterInputKeyword"
import type { PlatformPayer } from "./../../platform/PlatformPayer"

/** 추가 수수료 정책 다건 조회를 위한 필터 조건 */
export type PlatformAdditionalFeePolicyFilterInput = {
	/**
	 * 보관 조회 여부
	 *
	 * true 이면 보관된 추가 수수료 정책의 필터 옵션을 조회하고, false 이면 보관되지 않은 추가 수수료 정책의 필터 옵션을 조회합니다. 기본값은 false 입니다.
	 */
	isArchived?: boolean
	/**
	 * 금액 부담 주체
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 부가세 부담 주체에 해당하는 추가 수수료 정책만 조회합니다.
	 */
	vatPayers?: PlatformPayer[]
	/** 검색 키워드 */
	keyword?: PlatformAdditionalFeePolicyFilterInputKeyword
}

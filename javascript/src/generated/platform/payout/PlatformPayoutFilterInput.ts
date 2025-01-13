import type { Bank } from "./../../common/Bank"
import type { Currency } from "./../../common/Currency"
import type { PlatformPayoutFilterInputCriteria } from "./../../platform/payout/PlatformPayoutFilterInputCriteria"
import type { PlatformPayoutStatus } from "./../../platform/payout/PlatformPayoutStatus"
/** 지급 내역 필터 입력 정보 */
export type PlatformPayoutFilterInput = {
	/**
	 * 지급 상태
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 지급 상태를 가진 지급 내역을 조회합니다.
	 */
	statuses?: PlatformPayoutStatus[]
	/**
	 * 파트너 아이디
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 파트너 아이디를 가진 지급 내역을 조회합니다.
	 */
	partnerIds?: string[]
	/** 조회 기준 */
	criteria: PlatformPayoutFilterInputCriteria
	/**
	 * 지급 계좌 은행
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 지급 계좌 은행을 가진 지급 내역을 조회합니다.
	 */
	payoutAccountBanks?: Bank[]
	/**
	 * 파트너 태그
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 파트너 태그를 하나 이상 가진 지급 내역을 조회합니다.
	 */
	partnerTags?: string[]
	/**
	 * 지급 통화
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 지급 통화를 가진 지급 내역을 조회합니다.
	 */
	payoutCurrencies?: Currency[]
}

import type { Bank } from "#generated/common/Bank"
import type { Currency } from "#generated/common/Currency"
import type { PlatformAccountStatus } from "#generated/platform/PlatformAccountStatus"

/**
 * 플랫폼 정산 계좌
 *
 * `currency` 가 KRW 일 경우 예금주 조회 API 를 통해 올바른 계좌인지 검증합니다. 그 외의 화폐일 경우 따로 검증하지는 않습니다.
 */
export type PlatformAccount = {
	/** 은행 */
	bank: Bank
	/** 정산에 사용할 통화 */
	currency: Currency
	/** 계좌번호 */
	number: string
	/** 예금주명 */
	holder: string
	/** 계좌 상태 */
	status: PlatformAccountStatus
}

import type { Currency } from "#generated/common/Currency"
import type { DateRange } from "#generated/platform/DateRange"
import type { PlatformContract } from "#generated/platform/PlatformContract"
import type { PlatformOrderSettlementAmount } from "#generated/platform/PlatformOrderSettlementAmount"
import type { PlatformPartner } from "#generated/platform/PlatformPartner"
import type { PlatformPartnerSettlementStatus } from "#generated/platform/partnerSettlement/PlatformPartnerSettlementStatus"

export type PlatformPartnerOrderSettlement = {
	type: "ORDER"
	/** 정산내역 아이디 */
	id: string
	graphqlId: string
	/** 파트너 */
	partner: PlatformPartner
	/**
	 * 정산 일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 */
	settlementDate: string
	/** 정산 통화 */
	settlementCurrency: Currency
	/** 정산 상태 */
	status: PlatformPartnerSettlementStatus
	/** 메모 */
	memo?: string
	/** 계약 */
	contract: PlatformContract
	/** 정산 시작 일 범위 */
	settlementStartDateRange: DateRange
	/** 금액 정보 */
	amount: PlatformOrderSettlementAmount
	/** 테스트 모드 여부 */
	isForTest: boolean
}
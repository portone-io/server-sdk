import type { Currency } from "./../../common/Currency"
import type { PlatformPartner } from "./../../platform/PlatformPartner"
import type { PlatformTransferStatus } from "./../../platform/transfer/PlatformTransferStatus"
import type { PlatformUserDefinedPropertyKeyValue } from "./../../platform/transfer/PlatformUserDefinedPropertyKeyValue"
/** 수기 정산건 */
export type PlatformManualTransfer = {
	type: "MANUAL"
	/** 정산건 아이디 */
	id: string
	graphqlId: string
	/** 파트너 */
	partner: PlatformPartner
	/** 정산 상태 */
	status: PlatformTransferStatus
	/** 메모 */
	memo?: string
	/**
	 * 정산 일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 * (yyyy-MM-dd)
	 */
	settlementDate: string
	/** 정산 통화 */
	settlementCurrency: Currency
	payoutId?: string
	payoutGraphqlId?: string
	/** 테스트 모드 여부 */
	isForTest: boolean
	/** 사용자 정의 속성 */
	userDefinedProperties: PlatformUserDefinedPropertyKeyValue[]
	/**
	 * 정산 금액
	 * (int64)
	 */
	settlementAmount: number
}

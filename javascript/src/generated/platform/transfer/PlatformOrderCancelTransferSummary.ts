import type { Currency } from "./../../common/Currency"
import type { PlatformOrderSettlementAmount } from "./../../platform/PlatformOrderSettlementAmount"
import type { PlatformTransferStatus } from "./../../platform/transfer/PlatformTransferStatus"
import type { PlatformTransferSummaryPartner } from "./../../platform/transfer/PlatformTransferSummaryPartner"
import type { PlatformTransferSummaryPayment } from "./../../platform/transfer/PlatformTransferSummaryPayment"
import type { PlatformUserDefinedPropertyKeyValue } from "./../../platform/transfer/PlatformUserDefinedPropertyKeyValue"
export type PlatformOrderCancelTransferSummary = {
	type: "ORDER_CANCEL"
	id: string
	graphqlId: string
	storeId: string
	partner: PlatformTransferSummaryPartner
	status: PlatformTransferStatus
	memo?: string
	/**
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 * (yyyy-MM-dd)
	 */
	settlementDate: string
	settlementCurrency: Currency
	isForTest: boolean
	/** 사용자 정의 속성 */
	partnerUserDefinedProperties: PlatformUserDefinedPropertyKeyValue[]
	/** 사용자 정의 속성 */
	userDefinedProperties: PlatformUserDefinedPropertyKeyValue[]
	amount: PlatformOrderSettlementAmount
	payment: PlatformTransferSummaryPayment
	/**
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 * (yyyy-MM-dd)
	 */
	settlementStartDate: string
}

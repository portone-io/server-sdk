import type { Currency } from "#generated/common/Currency"
import type { PlatformOrderSettlementAmount } from "#generated/platform/PlatformOrderSettlementAmount"
import type { PlatformTransferStatus } from "#generated/platform/transfer/PlatformTransferStatus"
import type { PlatformTransferSummaryPartner } from "#generated/platform/transfer/PlatformTransferSummaryPartner"
import type { PlatformTransferSummaryPayment } from "#generated/platform/transfer/PlatformTransferSummaryPayment"
import type { PlatformUserDefinedPropertyKeyValue } from "#generated/platform/transfer/PlatformUserDefinedPropertyKeyValue"

export type PlatformOrderCancelTransferSummary = {
	type: "ORDER_CANCEL"
	id: string
	graphqlId: string
	storeId: string
	partner: PlatformTransferSummaryPartner
	status: PlatformTransferStatus
	memo?: string
	/** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
	settlementDate: string
	settlementCurrency: Currency
	isForTest: boolean
	/** 사용자 정의 속성 */
	partnerUserDefinedProperties: PlatformUserDefinedPropertyKeyValue[]
	/** 사용자 정의 속성 */
	userDefinedProperties: PlatformUserDefinedPropertyKeyValue[]
	amount: PlatformOrderSettlementAmount
	payment: PlatformTransferSummaryPayment
	/** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
	settlementStartDate: string
}

import type { Currency } from "./../../common/Currency"
import type { PlatformPartner } from "./../../platform/PlatformPartner"
import type { PlatformPayoutAccount } from "./../../platform/payout/PlatformPayoutAccount"
import type { PlatformPayoutMethod } from "./../../platform/PlatformPayoutMethod"
import type { PlatformPayoutStatus } from "./../../platform/payout/PlatformPayoutStatus"
import type { SettlementAmountType } from "./../../platform/SettlementAmountType"
export type PlatformPayout = {
	/** 지급 고유 아이디 */
	id: string
	graphqlId: string
	method: PlatformPayoutMethod
	status: PlatformPayoutStatus
	/** (RFC 3339 date-time) */
	statusUpdatedAt: string
	memo?: string
	partner: PlatformPartner
	account: PlatformPayoutAccount
	currency: Currency
	/**
	 * 지급금액
	 * (int64)
	 */
	amount: number
	/**
	 * 공급가액
	 * (int64)
	 */
	supplyAmount: number
	/**
	 * 면세 금액
	 * (int64)
	 */
	taxFreeAmount: number
	/**
	 * 부가세
	 * (int64)
	 */
	vatAmount: number
	/**
	 * 정산 금액
	 * (int64)
	 */
	settlementAmount: number
	/**
	 * 정산 면세 금액
	 * (int64)
	 */
	settlementTaxFreeAmount: number
	/**
	 * 원천징수세액 (소득세)
	 * (int64)
	 */
	incomeTaxAmount: number
	/**
	 * 원천징수세액 (지방소득세)
	 * (int64)
	 */
	localIncomeTaxAmount: number
	withdrawalMemo?: string
	depositMemo?: string
	/** (RFC 3339 date-time) */
	createdAt: string
	/** (RFC 3339 date-time) */
	scheduledAt?: string
	/** 실패 사유 */
	failReason?: string
	/** 지급 금액에서 원천징수세 차감 여부 */
	deductWht: boolean
	/** 정산 금액 취급 기준 */
	settlementAmountType: SettlementAmountType
}

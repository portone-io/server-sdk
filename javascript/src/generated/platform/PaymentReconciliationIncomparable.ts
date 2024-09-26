import type { Currency } from "#generated/common/Currency"
import type { PaymentReconciliationActionType } from "#generated/platform/PaymentReconciliationActionType"
import type { ReconciliationPaymentMethod } from "#generated/platform/ReconciliationPaymentMethod"
import type { ReconciliationPgSpecifier } from "#generated/platform/ReconciliationPgSpecifier"
import type { Settlement } from "#generated/platform/Settlement"

export type PaymentReconciliationIncomparable = {
	status: "INCOMPARABLE"
	/** 거래대사 아이디 */
	id: string
	graphqlId: string
	actionType: PaymentReconciliationActionType
	/** 대사용 PG사 가맹점 식별자 */
	pgSpecifier: ReconciliationPgSpecifier
	/** 고객사 아이디 */
	merchantId: string
	merchantGraphqlId: string
	/**
	 * 결제 금액
	 * (int64)
	 */
	paymentAmount: number
	/**
	 * 면세가액
	 * (int64)
	 */
	taxFreeAmount: number
	/**
	 * 부가세
	 * (int64)
	 */
	vatAmount: number
	/**
	 * 공급가액
	 * (int64)
	 */
	supplyAmount: number
	/**
	 * 거래이상 금액
	 * (int64)
	 */
	anomalyAmount: number
	/**
	 * 결제일
	 * (RFC 3339 date-time)
	 */
	paidAt: string
	/** 에스크로 여부 */
	isEscrow?: boolean
	/** 결제 통화 */
	paymentCurrency: Currency
	/** 결제수단 상세 정보 */
	paymentMethod: ReconciliationPaymentMethod
	/** PG사 거래 아이디 */
	pgTxId: string
	/** 거래건의 정산 정보 */
	settlement?: Settlement
}

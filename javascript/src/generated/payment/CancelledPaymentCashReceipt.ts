import type { CashReceiptType } from "./../common/CashReceiptType"
import type { Currency } from "./../common/Currency"
/** 취소된 현금영수증 */
export type CancelledPaymentCashReceipt = {
	/** 결제 건 내 현금영수증 상태 */
	status: "CANCELLED"
	/** 현금영수증 유형 */
	type?: CashReceiptType
	/** PG사 영수증 발급 아이디 */
	pgReceiptId?: string
	/** 승인 번호 */
	issueNumber: string
	/**
	 * 총 금액
	 * (int64)
	 */
	totalAmount: number
	/**
	 * 면세액
	 * (int64)
	 */
	taxFreeAmount?: number
	/** 통화 */
	currency: Currency
	/** 현금영수증 URL */
	url?: string
	/**
	 * 발급 시점
	 * (RFC 3339 date-time)
	 */
	issuedAt: string
	/**
	 * 취소 시점
	 * (RFC 3339 date-time)
	 */
	cancelledAt: string
}

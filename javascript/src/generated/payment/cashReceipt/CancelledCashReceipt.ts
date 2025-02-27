import type { CashReceiptType } from "./../../common/CashReceiptType"
import type { Currency } from "./../../common/Currency"
import type { SelectedChannel } from "./../../common/SelectedChannel"
/** 발급 취소 */
export type CancelledCashReceipt = {
	/** 현금영수증 상태 */
	status: "CANCELLED"
	/** 고객사 아이디 */
	merchantId: string
	/** 상점 아이디 */
	storeId: string
	/** 결제 건 아이디 */
	paymentId: string
	/** 현금영수증 발급에 사용된 채널 */
	channel: SelectedChannel
	/**
	 * 결제 금액
	 * (int64)
	 */
	amount: number
	/**
	 * 면세액
	 * (int64)
	 */
	taxFreeAmount?: number
	/**
	 * 부가세액
	 * (int64)
	 */
	vatAmount?: number
	/** 통화 */
	currency: Currency
	/** 주문명 */
	orderName: string
	/** 수동 발급 여부 */
	isManual: boolean
	/** 현금영수증 유형 */
	type?: CashReceiptType
	/** PG사 현금영수증 아이디 */
	pgReceiptId?: string
	/** 승인번호 */
	issueNumber: string
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
	/**
	 * 상태 업데이트 시점
	 * (RFC 3339 date-time)
	 */
	statusUpdatedAt?: string
}

import type { Trigger } from "./../payment/Trigger"
/** 취소 요청 상태 */
export type RequestedPaymentCancellation = {
	/** 결제 취소 내역 상태 */
	status: "REQUESTED"
	/** 취소 내역 아이디 */
	id: string
	/** PG사 결제 취소 내역 아이디 */
	pgCancellationId?: string
	/**
	 * 취소 총 금액
	 * (int64)
	 */
	totalAmount: number
	/**
	 * 취소 금액 중 면세 금액
	 * (int64)
	 */
	taxFreeAmount: number
	/**
	 * 취소 금액 중 부가세액
	 * (int64)
	 */
	vatAmount: number
	/**
	 * 적립형 포인트의 환불 금액
	 * (int64)
	 */
	easyPayDiscountAmount?: number
	/** 취소 사유 */
	reason: string
	/**
	 * 취소 시점
	 * (RFC 3339 date-time)
	 */
	cancelledAt?: string
	/**
	 * 취소 요청 시점
	 * (RFC 3339 date-time)
	 */
	requestedAt: string
	/** 취소 요청 경로 */
	trigger?: Trigger
}

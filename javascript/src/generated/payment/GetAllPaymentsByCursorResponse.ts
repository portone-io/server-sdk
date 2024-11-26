import type { PaymentWithCursor } from "./../payment/PaymentWithCursor"
/** 결제 건 커서 기반 대용량 다건 조회 성공 응답 정보 */
export type GetAllPaymentsByCursorResponse = {
	/** 조회된 결제 건 및 커서 정보 리스트 */
	items: PaymentWithCursor[]
}

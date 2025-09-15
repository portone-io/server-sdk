import type { PaymentEventWithCursor } from "./../payment/PaymentEventWithCursor"
/** 결제 이벤트 커서 기반 대용량 다건 조회 성공 응답 정보 */
export type GetAllPaymentEventsByCursorResponse = {
	/** 조회된 결제 이벤트 및 커서 정보 리스트 */
	items: PaymentEventWithCursor[]
}

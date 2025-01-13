import type { PaymentTransaction } from "./../payment/PaymentTransaction"
/** 결제 시도 내역 조회 응답 정보 */
export type GetPaymentTransactionsResponse = {
	/** 결제 시도 내역 */
	items: PaymentTransaction[]
}

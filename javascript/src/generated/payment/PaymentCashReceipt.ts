import type { CancelledPaymentCashReceipt } from "#generated/payment/CancelledPaymentCashReceipt"
import type { IssuedPaymentCashReceipt } from "#generated/payment/IssuedPaymentCashReceipt"

/** 결제 건 내 현금영수증 정보 */
export type PaymentCashReceipt =
	/** 발급 취소 */
	| CancelledPaymentCashReceipt
	/** 발급 완료 */
	| IssuedPaymentCashReceipt

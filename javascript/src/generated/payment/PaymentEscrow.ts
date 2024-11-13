import type { BeforeRegisteredPaymentEscrow } from "./../payment/BeforeRegisteredPaymentEscrow"
import type { CancelledPaymentEscrow } from "./../payment/CancelledPaymentEscrow"
import type { ConfirmedPaymentEscrow } from "./../payment/ConfirmedPaymentEscrow"
import type { DeliveredPaymentEscrow } from "./../payment/DeliveredPaymentEscrow"
import type { RegisteredPaymentEscrow } from "./../payment/RegisteredPaymentEscrow"
import type { RejectConfirmedPaymentEscrow } from "./../payment/RejectConfirmedPaymentEscrow"
import type { RejectedPaymentEscrow } from "./../payment/RejectedPaymentEscrow"

/**
 * 에스크로 정보
 *
 * V1 결제 건의 경우 타입이 REGISTERED 로 고정됩니다.
 */
export type PaymentEscrow =
	/** 배송 정보 등록 전 */
	| BeforeRegisteredPaymentEscrow
	/** 거래 취소 */
	| CancelledPaymentEscrow
	/** 구매 확정 */
	| ConfirmedPaymentEscrow
	/** 배송 완료 */
	| DeliveredPaymentEscrow
	/** 배송 정보 등록 완료 */
	| RegisteredPaymentEscrow
	/** 구매 거절 */
	| RejectedPaymentEscrow
	/** 구매 거절 확정 */
	| RejectConfirmedPaymentEscrow
	| { readonly status: unique symbol }

import type { PaymentMethodCard } from "./../payment/PaymentMethodCard"
import type { PaymentMethodEasyPayMethodCharge } from "./../payment/PaymentMethodEasyPayMethodCharge"
import type { PaymentMethodTransfer } from "./../payment/PaymentMethodTransfer"

/** 간편 결제 수단 */
export type PaymentMethodEasyPayMethod =
	/** 결제수단 카드 정보 */
	| PaymentMethodCard
	/** 충전식 포인트 결제 정보 */
	| PaymentMethodEasyPayMethodCharge
	/** 계좌 이체 상세 정보 */
	| PaymentMethodTransfer
	| { readonly type: unique symbol }

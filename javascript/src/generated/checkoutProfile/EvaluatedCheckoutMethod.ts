import type { CheckoutPaymentMethod } from "./../common/CheckoutPaymentMethod"
/** 결제 수단 */
export type EvaluatedCheckoutMethod = {
	/** 결제수단 */
	paymentMethod: CheckoutPaymentMethod
	/** 채널 키 */
	channelKey: string
}

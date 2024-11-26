import type { EasyPayProvider } from "./../common/EasyPayProvider"
import type { PaymentMethodEasyPayMethod } from "./../payment/PaymentMethodEasyPayMethod"
/** 간편 결제 상세 정보 */
export type PaymentMethodEasyPay = {
	type: "PaymentMethodEasyPay"
	/** 간편 결제 PG사 */
	provider?: EasyPayProvider
	/** 간편 결제 수단 */
	easyPayMethod?: PaymentMethodEasyPayMethod
}

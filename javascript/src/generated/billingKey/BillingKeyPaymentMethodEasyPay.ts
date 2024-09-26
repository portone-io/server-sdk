import type { BillingKeyPaymentMethodEasyPayMethod } from "#generated/billingKey/BillingKeyPaymentMethodEasyPayMethod"
import type { EasyPayProvider } from "#generated/common/EasyPayProvider"

/** 간편 결제 정보 */
export type BillingKeyPaymentMethodEasyPay = {
	type: "BillingKeyPaymentMethodEasyPay"
	/** 간편 결제 PG사 */
	provider?: EasyPayProvider
	/** 간편 결제 수단 */
	method?: BillingKeyPaymentMethodEasyPayMethod
}

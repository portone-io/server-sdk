import type { ReconciliationEasyPayMethod } from "#generated/platform/ReconciliationEasyPayMethod"
import type { ReconciliationEasyPayProvider } from "#generated/platform/ReconciliationEasyPayProvider"

/** 간편 결제 */
export type ReconciliationPaymentMethodEasyPay = {
	/** 대사용 결제 수단 */
	type: "EASY_PAY"
	/** 간편 결제 PG사 */
	provider?: ReconciliationEasyPayProvider
	/** 간편 결제 결제 수단 */
	method?: ReconciliationEasyPayMethod
}

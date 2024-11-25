import type { Currency } from "./../../common/Currency"
import type { PaymentMethodType } from "./../../common/PaymentMethodType"
export type PlatformTransferSummaryExternalPayment = {
	type: "EXTERNAL"
	id: string
	orderName?: string
	currency: Currency
	methodType?: PaymentMethodType
}

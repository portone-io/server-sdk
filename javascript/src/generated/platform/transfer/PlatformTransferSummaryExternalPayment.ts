import type { Currency } from "#generated/common/Currency"
import type { PaymentMethodType } from "#generated/common/PaymentMethodType"

export type PlatformTransferSummaryExternalPayment = {
	type: "EXTERNAL"
	id: string
	orderName?: string
	currency: Currency
	methodType?: PaymentMethodType
}

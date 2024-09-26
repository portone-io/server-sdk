import type { Currency } from "#generated/common/Currency"
import type { PaymentMethodType } from "#generated/common/PaymentMethodType"

export type PlatformTransferSummaryPortOnePayment = {
	type: "PORT_ONE"
	id: string
	orderName: string
	currency: Currency
	methodType?: PaymentMethodType
}

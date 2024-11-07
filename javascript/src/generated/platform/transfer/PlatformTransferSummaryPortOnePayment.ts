import type { Currency } from "./../../common/Currency"
import type { PaymentMethodType } from "./../../common/PaymentMethodType"

export type PlatformTransferSummaryPortOnePayment = {
	type: "PORT_ONE"
	id: string
	orderName: string
	currency: Currency
	methodType?: PaymentMethodType
}

import type { Currency } from "./../../common/Currency"
import type { PlatformPaymentMethod } from "./../../platform/transfer/PlatformPaymentMethod"
/** 외부 결제 정보 */
export type PlatformExternalPayment = {
	type: "EXTERNAL"
	/** 결제 아이디 */
	id: string
	/** 주문 명 */
	orderName?: string
	/** 통화 */
	currency: Currency
	/** 결제 수단 */
	method?: PlatformPaymentMethod
	/**
	 * 결제 일시
	 * (RFC 3339 date-time)
	 */
	paidAt?: string
}

import type { Currency } from "./../../common/Currency"
import type { PlatformPaymentMethod } from "./../../platform/transfer/PlatformPaymentMethod"

/** 포트원 결제 정보 */
export type PlatformPortOnePayment = {
	type: "PORT_ONE"
	/** 결제 아이디 */
	id: string
	/** 상점 아이디 */
	storeId: string
	/** 채널 키 */
	channelKey: string
	/** 주문 명 */
	orderName: string
	/** 결제 수단 */
	method?: PlatformPaymentMethod
	/** 통화 */
	currency: Currency
	/**
	 * 결제 일시
	 * (RFC 3339 date-time)
	 */
	paidAt: string
}

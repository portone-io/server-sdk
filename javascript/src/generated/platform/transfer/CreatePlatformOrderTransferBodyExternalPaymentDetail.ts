import type { Currency } from "#generated/common/Currency"
import type { PlatformPaymentMethodInput } from "#generated/platform/transfer/PlatformPaymentMethodInput"

/** 외부 결제 상세 정보 */
export type CreatePlatformOrderTransferBodyExternalPaymentDetail = {
	/** 통화 */
	currency: Currency
	/** 주문 명 */
	orderName?: string
	/**
	 * 결제 일시
	 * (RFC 3339 date-time)
	 */
	paidAt?: string
	/** 결제 수단 */
	method?: PlatformPaymentMethodInput
}

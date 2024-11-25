import type { PaymentLogisticsCompany } from "./../payment/PaymentLogisticsCompany"
import type { SeparatedAddressInput } from "./../common/SeparatedAddressInput"
/** 배송정보 */
export type PaymentLogistics = {
	/** 물류회사 */
	company: PaymentLogisticsCompany
	/** 송장번호 */
	invoiceNumber: string
	/**
	 * 발송시점
	 * (RFC 3339 date-time)
	 */
	sentAt: string
	/**
	 * 수령시점
	 * (RFC 3339 date-time)
	 */
	receivedAt?: string
	/** 주소 */
	address?: SeparatedAddressInput
}

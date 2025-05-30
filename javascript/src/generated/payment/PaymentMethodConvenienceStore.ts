import type { ConvenienceStoreBrand } from "./../payment/ConvenienceStoreBrand"
/** 편의점 결제 상세 정보 */
export type PaymentMethodConvenienceStore = {
	type: "PaymentMethodConvenienceStore"
	/** 편의점 브랜드 */
	convenienceStoreBrand?: ConvenienceStoreBrand
	/** 결제 확인 번호 */
	confirmationNumber?: string
	/** 결제 접수 번호 */
	receiptNumber?: string
	/**
	 * 결제 마감 시간
	 * (RFC 3339 date-time)
	 */
	paymentDeadline?: string
}

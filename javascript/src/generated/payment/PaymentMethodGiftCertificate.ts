import type { PaymentMethodGiftCertificateType } from "#generated/payment/PaymentMethodGiftCertificateType"

/** 상품권 상세 정보 */
export type PaymentMethodGiftCertificate = {
	type: "PaymentMethodGiftCertificate"
	/** 상품권 종류 */
	giftCertificateType?: PaymentMethodGiftCertificateType
	/** 상품권 승인 번호 */
	approvalNumber: string
}

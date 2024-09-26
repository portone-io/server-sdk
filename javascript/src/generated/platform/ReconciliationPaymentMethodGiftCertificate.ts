import type { GiftCertificateType } from "#generated/platform/GiftCertificateType"

/** 상품권 결제 */
export type ReconciliationPaymentMethodGiftCertificate = {
	/** 대사용 결제 수단 */
	type: "GIFT_CERTIFICATE"
	/** 상품권 승인 번호 */
	approvalNumber?: string
	/** 상품권 종류 */
	giftCertificateType?: GiftCertificateType
}

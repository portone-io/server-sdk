import type { CashReceiptInputType } from "#generated/common/CashReceiptInputType"

/** 가상계좌 결제 시 현금영수증 정보 */
export type InstantPaymentMethodInputVirtualAccountCashReceiptInfo = {
	/** 현금영수증 유형 */
	type: CashReceiptInputType
	/** 사용자 식별 번호 */
	customerIdentityNumber: string
}

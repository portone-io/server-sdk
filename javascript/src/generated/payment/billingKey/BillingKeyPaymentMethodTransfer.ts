import type { Bank } from "./../../common/Bank"
/** 계좌이체 정보 */
export type BillingKeyPaymentMethodTransfer = {
	type: "BillingKeyPaymentMethodTransfer"
	/** 표준 은행 코드 */
	bank?: Bank
	/** 계좌번호 */
	accountNumber?: string
}

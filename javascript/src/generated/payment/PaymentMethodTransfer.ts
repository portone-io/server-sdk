import type { Bank } from "./../common/Bank"
/** 계좌 이체 상세 정보 */
export type PaymentMethodTransfer = {
	type: "PaymentMethodTransfer"
	/** 표준 은행 코드 */
	bank?: Bank
}

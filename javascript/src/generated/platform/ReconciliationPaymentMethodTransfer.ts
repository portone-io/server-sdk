import type { Bank } from "#generated/common/Bank"

/** 계좌이체 */
export type ReconciliationPaymentMethodTransfer = {
	/** 대사용 결제 수단 */
	type: "TRANSFER"
	/** 계좌 이체 은행 */
	bank?: Bank
	/** 계좌 이체 승인 번호 */
	approvalNumber?: string
}

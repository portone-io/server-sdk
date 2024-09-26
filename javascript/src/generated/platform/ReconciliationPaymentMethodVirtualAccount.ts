import type { Bank } from "#generated/common/Bank"

/** 가상계좌 결제 */
export type ReconciliationPaymentMethodVirtualAccount = {
	/** 대사용 결제 수단 */
	type: "VIRTUAL_ACCOUNT"
	/** 가상계좌  은행 */
	bank?: Bank
	/** 가상계좌 은행 */
	approvalNumber?: string
}

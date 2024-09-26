import type { ReconciliationDateConditionInput } from "#generated/platform/ReconciliationDateConditionInput"

export type GetPaymentReconciliationsBody = {
	dateCondition: ReconciliationDateConditionInput
	/**
	 * 조회할 건 수
	 * (int32)
	 */
	size: number
	/** 이전 페이지의 마지막 커서 */
	after?: string
}

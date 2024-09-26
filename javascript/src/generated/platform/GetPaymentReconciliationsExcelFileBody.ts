import type { PaymentReconciliationColumn } from "#generated/platform/PaymentReconciliationColumn"
import type { PaymentReconciliationExcelFileFilterInput } from "#generated/platform/PaymentReconciliationExcelFileFilterInput"
import type { PaymentReconciliationOrderInput } from "#generated/platform/PaymentReconciliationOrderInput"
import type { PaymentReconciliationSearchConditionInput } from "#generated/platform/PaymentReconciliationSearchConditionInput"
import type { ReconciliationDateConditionInput } from "#generated/platform/ReconciliationDateConditionInput"

export type GetPaymentReconciliationsExcelFileBody = {
	/** 엑셀파일 요청시 선택 필드 */
	columns: PaymentReconciliationColumn[]
	dateCondition: ReconciliationDateConditionInput
	searchCondition?: PaymentReconciliationSearchConditionInput
	filter?: PaymentReconciliationExcelFileFilterInput
	order?: PaymentReconciliationOrderInput
}

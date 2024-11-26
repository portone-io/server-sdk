import type { Unrecognized } from "./../../../utils/unrecognized"
import type { CancelledCashReceipt } from "./../../payment/cashReceipt/CancelledCashReceipt"
import type { IssueFailedCashReceipt } from "./../../payment/cashReceipt/IssueFailedCashReceipt"
import type { IssuedCashReceipt } from "./../../payment/cashReceipt/IssuedCashReceipt"
/** 현금영수증 내역 */
export type CashReceipt =
	/** 발급 취소 */
	| CancelledCashReceipt
	/** 발급 완료 */
	| IssuedCashReceipt
	/** 발급 실패 */
	| IssueFailedCashReceipt
	| { readonly status: Unrecognized }

export function isUnrecognizedCashReceipt(entity: CashReceipt): entity is { readonly status: Unrecognized } {
	return entity.status !== "CANCELLED"
		&& entity.status !== "ISSUED"
		&& entity.status !== "ISSUE_FAILED"
}

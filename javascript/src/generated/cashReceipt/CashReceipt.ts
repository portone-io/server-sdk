import type { CancelledCashReceipt } from "#generated/cashReceipt/CancelledCashReceipt"
import type { IssueFailedCashReceipt } from "#generated/cashReceipt/IssueFailedCashReceipt"
import type { IssuedCashReceipt } from "#generated/cashReceipt/IssuedCashReceipt"

/** 현금영수증 내역 */
export type CashReceipt =
	/** 발급 취소 */
	| CancelledCashReceipt
	/** 발급 완료 */
	| IssuedCashReceipt
	/** 발급 실패 */
	| IssueFailedCashReceipt

/** 현금영수증 내역 */
export type CashReceiptSummary = {
	/** 발행 번호 */
	issueNumber: string
	/** 현금 영수증 URL */
	url: string
	/** PG사 현금영수증 아이디 */
	pgReceiptId: string
}

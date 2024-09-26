/** 세금계산서 첨부파일 */
export type B2bTaxInvoiceAttachment = {
	/** 첨부 파일 아이디 */
	id: string
	/** 첨부 파일명 */
	name: string
	/**
	 * 첨부 일시
	 * (RFC 3339 date-time)
	 */
	attachedAt: string
}

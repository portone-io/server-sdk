import type { B2bTaxInvoiceAttachment } from "#generated/b2b/B2bTaxInvoiceAttachment"

/** 세금계산서 첨부파일 목록 조회 성공 응답 */
export type GetB2bTaxInvoiceAttachmentsResponse = {
	/** 첨부파일 목록 */
	attachments: B2bTaxInvoiceAttachment[]
}

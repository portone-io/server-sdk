import type { GetB2bTaxInvoicesBodyDateFilter } from "#generated/b2b/TaxInvoice/GetB2bTaxInvoicesBodyDateFilter"

/**
 * 상위 필터
 *
 * 주어진 필드 중 한 개의 필드만 입력합니다.
 */
export type GetB2bTaxInvoicesBodyPrimaryFilter = {
	/** 조회 기간 */
	dateFilter?: GetB2bTaxInvoicesBodyDateFilter
	/** 세금계산서 아이디 */
	taxInvoiceId?: string
	/** 일괄발행 아이디 */
	bulkTaxInvoiceId?: string
	/** 국세청 승인번호 */
	ntsApprovalNumber?: string
	/** 공급자 문서번호 */
	supplierDocumentKey?: string
	/** 공급받는자 승인번호 */
	recipientDocumentKey?: string
	/** 세금계산서 아이디 리스트 */
	taxInvoiceIds?: string[]
}

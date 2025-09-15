import type { B2bTaxInvoiceContact } from "./../../b2b/taxInvoice/B2bTaxInvoiceContact"
export type B2bTaxInvoiceCompany = {
	/**
	 * 사업자등록번호
	 *
	 * `-`를 제외한 10자리
	 */
	brn: string
	/**
	 * 종사업자 식별 번호
	 *
	 * 4자리 고정
	 */
	taxRegistrationId?: string
	/**
	 * 상호명
	 *
	 * 최대 200자
	 */
	name: string
	/**
	 * 대표자 성명
	 *
	 * 최대 100자
	 */
	representativeName: string
	/**
	 * 주소
	 *
	 * 최대 300자
	 */
	address?: string
	/**
	 * 업태
	 *
	 * 최대 100자
	 */
	businessType?: string
	/**
	 * 종목
	 *
	 * 최대 100자
	 */
	businessClass?: string
	/** 담당자 */
	contact: B2bTaxInvoiceContact
}

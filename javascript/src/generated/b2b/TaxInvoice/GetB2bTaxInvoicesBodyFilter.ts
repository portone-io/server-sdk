import type { B2bTaxInvoiceDocumentModificationType } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceDocumentModificationType"
import type { B2bTaxInvoiceIssuanceType } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceIssuanceType"
import type { B2bTaxInvoicePurposeType } from "#generated/b2b/TaxInvoice/B2bTaxInvoicePurposeType"
import type { B2bTaxInvoiceStatus } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceStatus"
import type { B2bTaxInvoiceTaxationType } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceTaxationType"
import type { GetB2bTaxInvoicesBodyPrimaryFilter } from "#generated/b2b/TaxInvoice/GetB2bTaxInvoicesBodyPrimaryFilter"

/** 세금계산서 다건 조회 필터 */
export type GetB2bTaxInvoicesBodyFilter = {
	/**
	 * 상위 필터
	 *
	 * 가장 주요 항목을 설정하는 상위 필터이며 사용할 때는 주어진 필드 중 한 개의 필드만 입력합니다.
	 */
	primaryFilter?: GetB2bTaxInvoicesBodyPrimaryFilter
	/** 공급자 사업자등록번호 */
	supplierBrn?: string
	/**
	 * 세금계산서 상태
	 *
	 * 미입력시 모든 상태를 조회합니다.
	 */
	statuses?: B2bTaxInvoiceStatus[]
	/** 과세 유형 */
	taxationTypes?: B2bTaxInvoiceTaxationType[]
	/** 문서 유형 */
	documentModificationTypes?: B2bTaxInvoiceDocumentModificationType[]
	/** 지연 발행 여부 */
	isDelayed?: boolean
	/** 발행 유형 */
	issuanceTypes?: B2bTaxInvoiceIssuanceType[]
	/** 영수/청구 */
	purposeTypes?: B2bTaxInvoicePurposeType[]
}

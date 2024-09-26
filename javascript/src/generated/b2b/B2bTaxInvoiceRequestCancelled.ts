import type { B2bModification } from "#generated/b2b/B2bModification"
import type { B2bTaxInvoiceAdditionalContact } from "#generated/b2b/B2bTaxInvoiceAdditionalContact"
import type { B2bTaxInvoiceCompany } from "#generated/b2b/B2bTaxInvoiceCompany"
import type { B2bTaxInvoiceItem } from "#generated/b2b/B2bTaxInvoiceItem"
import type { B2bTaxInvoicePurposeType } from "#generated/b2b/B2bTaxInvoicePurposeType"
import type { B2bTaxType } from "#generated/b2b/B2bTaxType"

export type B2bTaxInvoiceRequestCancelled = {
	/** 세금계산서 상태 */
	status: "REQUEST_CANCELLED"
	/** 과세 유형 */
	taxType: B2bTaxType
	/** 일련번호 */
	serialNum?: string
	/**
	 * 책번호 - 권
	 *
	 * 입력 범위(4자리) : 0 ~ 9999
	 * (int32)
	 */
	bookVolume?: number
	/**
	 * 책번호 - 호
	 *
	 * 입력 범위(4자리) : 0 ~ 9999
	 * (int32)
	 */
	bookIssue?: number
	/**
	 * 작성일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 */
	writeDate: string
	/** 영수/청구 */
	purposeType: B2bTaxInvoicePurposeType
	/**
	 * 공급가액 합계
	 * (int64)
	 */
	supplyCostTotalAmount: number
	/**
	 * 세액 합계
	 * (int64)
	 */
	taxTotalAmount: number
	/**
	 * 합계 금액
	 * (int64)
	 */
	totalAmount: number
	/**
	 * 현금
	 * (int64)
	 */
	cashAmount?: number
	/**
	 * 수표
	 * (int64)
	 */
	checkAmount?: number
	/**
	 * 외상
	 * (int64)
	 */
	creditAmount?: number
	/**
	 * 수표
	 * (int64)
	 */
	noteAmount?: number
	/**
	 * 비고
	 *
	 * 최대 3개
	 */
	remarks: string[]
	/** 공급자 문서번호 */
	supplierDocumentKey?: string
	/** 공급자 */
	supplier: B2bTaxInvoiceCompany
	/** 공급받는자 문서번호 */
	recipientDocumentKey?: string
	/** 공급받는자 */
	recipient: B2bTaxInvoiceCompany
	/** 문자 전송 여부 */
	sendSms: boolean
	/** 수정 사유 기재 */
	modification?: B2bModification
	/**
	 * 품목
	 *
	 * 최대 99개
	 */
	items: B2bTaxInvoiceItem[]
	/**
	 * 추가 담당자
	 *
	 * 최대 3개
	 */
	contacts: B2bTaxInvoiceAdditionalContact[]
	/**
	 * 상태 변경 일시
	 * (RFC 3339 date-time)
	 */
	statusUpdatedAt: string
}

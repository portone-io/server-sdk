import type { B2bTaxInvoiceAdditionalContact } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceAdditionalContact"
import type { B2bTaxInvoiceCompany } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceCompany"
import type { B2bTaxInvoiceDocumentModificationType } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceDocumentModificationType"
import type { B2bTaxInvoiceIssuanceType } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceIssuanceType"
import type { B2bTaxInvoiceItem } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceItem"
import type { B2bTaxInvoiceModification } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceModification"
import type { B2bTaxInvoicePurposeType } from "#generated/b2b/TaxInvoice/B2bTaxInvoicePurposeType"
import type { B2bTaxInvoiceStatus } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceStatus"
import type { B2bTaxInvoiceTaxationType } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceTaxationType"

/** 세금계산서 */
export type B2bTaxInvoice = {
	/** 세금계산서 아이디 */
	id: string
	/** 상태 */
	status: B2bTaxInvoiceStatus
	/** 과세 유형 */
	taxationType: B2bTaxInvoiceTaxationType
	/** 문서 유형 */
	documentModificationType: B2bTaxInvoiceDocumentModificationType
	/** 지연 발행 여부 */
	isDelayed?: boolean
	/** 발행 유형 */
	issuanceType: B2bTaxInvoiceIssuanceType
	/** 일괄 발행 아이디 */
	bulkTaxInvoiceId?: string
	/** 일련번호 */
	serialNumber?: string
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
	/**
	 * 발행 마감일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 */
	issuanceDueDate: string
	/** 영수/청구 */
	purposeType: B2bTaxInvoicePurposeType
	/**
	 * 공급가액 합계
	 * (int64)
	 */
	totalSupplyAmount: number
	/**
	 * 세액 합계
	 * (int64)
	 */
	totalTaxAmount: number
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
	 * 어음
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
	sendSms?: boolean
	/** 수정 사유 기재 */
	modification?: B2bTaxInvoiceModification
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
	additionalContacts: B2bTaxInvoiceAdditionalContact[]
	/** 메모 */
	memo?: string
	/**
	 * 임시 저장 일시
	 * (RFC 3339 date-time)
	 */
	draftedAt?: string
	/**
	 * 발행 요청 일시
	 * (RFC 3339 date-time)
	 */
	requestedAt?: string
	/**
	 * 발행 일시
	 * (RFC 3339 date-time)
	 */
	issuedAt?: string
	/**
	 * 상태 변경 일시
	 * (RFC 3339 date-time)
	 */
	statusUpdatedAt?: string
	/**
	 * 국세청 전송 일시
	 * (RFC 3339 date-time)
	 */
	ntsSentAt?: string
	/**
	 * 국세청 승인번호
	 *
	 * 세금계산서 발행(전자서명) 시점에 자동으로 부여
	 */
	ntsApprovalNumber?: string
	/** 국세청 전송 결과 */
	ntsResult?: string
	/**
	 * 국세청 결과 코드
	 *
	 * 국세청 발급 결과 코드로 영문 3자리 + 숫자 3자리로 구성됨
	 */
	ntsResultCode?: string
	/**
	 * 국세청 결과 수신 일시
	 * (RFC 3339 date-time)
	 */
	ntsResultReceivedAt?: string
}

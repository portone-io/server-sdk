import type { B2bCompanyStateBusinessStatus } from "#generated/common/B2bCompanyStateBusinessStatus"
import type { B2bTaxInvoiceDocumentModificationType } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceDocumentModificationType"
import type { B2bTaxInvoiceIssuanceType } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceIssuanceType"
import type { B2bTaxInvoicePurposeType } from "#generated/b2b/TaxInvoice/B2bTaxInvoicePurposeType"
import type { B2bTaxInvoiceStatus } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceStatus"
import type { B2bTaxInvoiceTaxationType } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceTaxationType"

/** 세금계산서 요약 */
export type B2bTaxInvoiceSummary = {
	/** 세금계산서 아이디 */
	id: string
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
	/** 영수/청구 */
	purposeType: B2bTaxInvoicePurposeType
	/** 공급자 사업자등록번호 */
	supplierBrn: string
	/** 공급자 상호 */
	supplierName: string
	/** 공급자 대표자 성명 */
	supplierRepresentativeName: string
	/** 공급자 문서번호 */
	supplierDocumentKey?: string
	/** 공급받는자 사업자등록번호 */
	recipientBrn: string
	/** 공급받는자 상호 */
	recipientName: string
	/** 공급받는자 대표자 성명 */
	recipientRepresentativeName: string
	/** 공급받는자 문서번호 */
	recipientDocumentKey?: string
	/** 공급받는자 영업 상태 */
	recipientBusinessStatus?: B2bCompanyStateBusinessStatus
	/**
	 * 공급받는자 휴폐업일자
	 *
	 * 상태가 CLOSED, SUSPENDED 상태인 경우에만 결과값 반환
	 */
	recipientClosedSuspendedDate?: string
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
	/** 상태 */
	status: B2bTaxInvoiceStatus
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
	 * 개봉 일시
	 * (RFC 3339 date-time)
	 */
	openedAt?: string
	/**
	 * 상태 변경 일시
	 * (RFC 3339 date-time)
	 */
	statusUpdatedAt: string
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
	 * 국세청 결과 수신 일시
	 * (RFC 3339 date-time)
	 */
	ntsResultReceivedAt?: string
	/**
	 * 국세청 결과 코드
	 *
	 * 국세청 발급 결과 코드로 영문 3자리 + 숫자 3자리로 구성됨
	 */
	ntsResultCode?: string
	/** 메모 */
	memo?: string
}

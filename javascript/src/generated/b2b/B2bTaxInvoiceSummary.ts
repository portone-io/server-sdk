import type { B2bCompanyStateBusinessStatus } from "#generated/b2b/B2bCompanyStateBusinessStatus"
import type { B2bTaxInvoicePurposeType } from "#generated/b2b/B2bTaxInvoicePurposeType"
import type { B2bTaxInvoiceStatus } from "#generated/b2b/B2bTaxInvoiceStatus"
import type { B2bTaxType } from "#generated/b2b/B2bTaxType"

/** 세금계산서 요약 */
export type B2bTaxInvoiceSummary = {
	/** 과세 유형 */
	taxType: B2bTaxType
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
	/** 영수/청구 */
	purposeType: B2bTaxInvoicePurposeType
	/** 공급자 사업자등록번호 */
	supplierBrn: string
	/** 공급자 상호 */
	supplierName: string
	/** 공급자 문서번호 */
	supplierDocumentKey?: string
	/** 공급받는자 사업자등록번호 */
	recipientBrn: string
	/** 공급받는자 상호 */
	recipientName: string
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
	 * 발행 일시
	 * (RFC 3339 date-time)
	 */
	issuedAt?: string
	/**
	 * 개봉 일시
	 * (RFC 3339 date-time)
	 */
	openedAt?: string
	/** 상태 */
	status: B2bTaxInvoiceStatus
	/**
	 * 상태 변경 일시
	 * (RFC 3339 date-time)
	 */
	statusUpdatedAt: string
	/**
	 * 국세청 승인번호
	 *
	 * 세금계산서 발행(전자서명) 시점에 자동으로 부여
	 */
	ntsApproveNumber?: string
	/** 국세청 전송 결과 */
	ntsResult?: string
	/**
	 * 국세청 전송 일시
	 * (RFC 3339 date-time)
	 */
	ntsSentAt?: string
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
}

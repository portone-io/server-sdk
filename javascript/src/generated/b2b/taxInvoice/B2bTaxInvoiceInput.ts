import type { B2bTaxInvoiceAdditionalContact } from "./../../b2b/taxInvoice/B2bTaxInvoiceAdditionalContact"
import type { B2bTaxInvoiceCompany } from "./../../b2b/taxInvoice/B2bTaxInvoiceCompany"
import type { B2bTaxInvoiceIssuanceType } from "./../../b2b/taxInvoice/B2bTaxInvoiceIssuanceType"
import type { B2bTaxInvoiceItem } from "./../../b2b/taxInvoice/B2bTaxInvoiceItem"
import type { B2bTaxInvoicePurposeType } from "./../../b2b/taxInvoice/B2bTaxInvoicePurposeType"
import type { B2bTaxInvoiceTaxationType } from "./../../b2b/taxInvoice/B2bTaxInvoiceTaxationType"
/** 세금계산서 생성 요청 정보 */
export type B2bTaxInvoiceInput = {
	/** 과세 유형 */
	taxationType: B2bTaxInvoiceTaxationType
	/**
	 * 발행 유형
	 *
	 * 기본값은 역발행(REVERSE)입니다.
	 */
	issuanceType?: B2bTaxInvoiceIssuanceType
	/** 일련번호 */
	serialNumber?: string
	/**
	 * 권
	 * (int32)
	 */
	bookVolume?: number
	/**
	 * 호
	 * (int32)
	 */
	bookIssue?: number
	/**
	 * 작성일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 * (yyyy-MM-dd)
	 */
	writeDate: string
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
	remarks?: string[]
	/**
	 * 공급자 문서번호
	 *
	 * 영문 대소문자, 숫자, 특수문자('-','_')만 이용 가능
	 */
	supplierDocumentKey?: string
	/** 공급자 */
	supplier: B2bTaxInvoiceCompany
	/**
	 * 공급받는자 문서번호
	 *
	 * 영문 대소문자, 숫자, 특수문자('-','_')만 이용 가능
	 */
	recipientDocumentKey?: string
	/** 공급받는자 */
	recipient: B2bTaxInvoiceCompany
	/**
	 * 문자 전송 여부
	 *
	 * 공급자 담당자 휴대폰번호 {supplier.contact.mobile_phone_number} 값으로 문자 전송 전송시 포인트 차감되며, 실패시 환불 처리 기본값은 false
	 */
	sendSms?: boolean
	/**
	 * 품목
	 *
	 * 최대 99개
	 */
	items?: B2bTaxInvoiceItem[]
	/**
	 * 추가 담당자
	 *
	 * 최대 3개
	 */
	additionalContacts?: B2bTaxInvoiceAdditionalContact[]
}

import type { B2bTaxInvoiceInput } from "./../../b2b/taxInvoice/B2bTaxInvoiceInput"
import type { B2bTaxInvoiceModificationCreateBody } from "./../../b2b/taxInvoice/B2bTaxInvoiceModificationCreateBody"
/** 세금계산서 즉시 정발행 요청 정보 */
export type IssueB2bTaxInvoiceImmediatelyBody = {
	/** 세금계산서 생성 요청 정보 */
	taxInvoice: B2bTaxInvoiceInput
	/** 메모 */
	memo?: string
	/** 수정 세금계산서 입력 정보 */
	modification?: B2bTaxInvoiceModificationCreateBody
	/**
	 * 공급받는자 거래처 생성 여부
	 *
	 * true인 경우 공급받는자 정보로 거래처를 자동 생성합니다.
	 */
	createRecipientCounterparty?: boolean
}

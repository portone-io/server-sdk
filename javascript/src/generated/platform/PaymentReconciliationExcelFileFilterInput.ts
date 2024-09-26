import type { Currency } from "#generated/common/Currency"
import type { PaymentReconciliationActionType } from "#generated/platform/PaymentReconciliationActionType"
import type { PaymentReconciliationStatus } from "#generated/platform/PaymentReconciliationStatus"
import type { ReconciliationPaymentMethodType } from "#generated/platform/ReconciliationPaymentMethodType"
import type { ReconciliationPgSpecifier } from "#generated/platform/ReconciliationPgSpecifier"

/**
 * 거래대사 엑셀 파일 다운로드 필터 목록
 *
 * 필드 중복으로 적용됩니다.
 */
export type PaymentReconciliationExcelFileFilterInput = {
	/**
	 * 거래대사 하위 가맹점 아이디 필터
	 *
	 * storeId가 존재하지 않는 건을 검색하고 싶은 경우 빈 문자열을 포함시켜주세요.
	 */
	storeIds?: string[]
	/** 거래대사 결제사(PG) 식별자 필터 */
	pgSpecifiers?: ReconciliationPgSpecifier[]
	/** 거래대사 결제 수단 필터 */
	paymentMethodTypes?: ReconciliationPaymentMethodType[]
	/** 거래대사 대사 상태 필터 */
	paymentReconciliationStatuses?: PaymentReconciliationStatus[]
	/** 거래대사 결제 상태 필터 */
	actionTypes?: PaymentReconciliationActionType[]
	/** 거래대사 결제 통화 필터 */
	transactionCurrencies?: Currency[]
	/** 거래대사 정산 통화 필터 */
	settlementCurrencies?: Currency[]
}

import type { ReconciliationPgSpecifier } from "#generated/platform/ReconciliationPgSpecifier"

/**
 * 거래대사 정산 요약 엑셀 파일 필터
 *
 * 필드 중복으로 적용됩니다.
 */
export type PaymentReconciliationSettlementSummaryExcelFileFilterInput = {
	/** PG사 가맹점 식별자 필터 */
	pgSpecifiers?: ReconciliationPgSpecifier[]
	/**
	 * 하위 상점 아이디 필터
	 *
	 * storeId가 존재하지 않는 건을 검색하고 싶은 경우 빈 문자열을 포함시켜주세요.
	 */
	storeIds?: string[]
}

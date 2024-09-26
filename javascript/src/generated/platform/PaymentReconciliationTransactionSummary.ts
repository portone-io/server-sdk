import type { Currency } from "#generated/common/Currency"
import type { PaymentReconciliationTransactionSummaryAggregate } from "#generated/platform/PaymentReconciliationTransactionSummaryAggregate"
import type { PaymentReconciliationTransactionSummaryDetail } from "#generated/platform/PaymentReconciliationTransactionSummaryDetail"

/** 거래대사 거래내역 일별 요약 */
export type PaymentReconciliationTransactionSummary = {
	/**
	 * 거래일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 */
	date: string
	/** 거래 통화 */
	currency: Currency
	/** 거래내역 합산 데이터 */
	aggregate: PaymentReconciliationTransactionSummaryAggregate
	/** 거래내역 상세 데이터 목록 */
	details: PaymentReconciliationTransactionSummaryDetail[]
}

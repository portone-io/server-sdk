import type { Currency } from "#generated/common/Currency"
import type { PaymentReconciliationSettlementSummaryAggregate } from "#generated/platform/PaymentReconciliationSettlementSummaryAggregate"
import type { PaymentReconciliationSettlementSummaryDetail } from "#generated/platform/PaymentReconciliationSettlementSummaryDetail"

/** 거래대사 정산내역 일별 요약 */
export type PaymentReconciliationSettlementSummary = {
	/**
	 * 정산일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 */
	date: string
	/** 정산 통화 */
	settlementCurrency: Currency
	/** 결제 통화 */
	transactionCurrency: Currency
	/** 정산내역 합산 데이터 */
	aggregate: PaymentReconciliationSettlementSummaryAggregate
	/** 정산내역 일별 상세 데이터 목록 */
	details: PaymentReconciliationSettlementSummaryDetail[]
}

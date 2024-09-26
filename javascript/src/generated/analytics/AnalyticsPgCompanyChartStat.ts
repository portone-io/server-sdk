import type { PgCompany } from "#generated/common/PgCompany"

/** 결제대행사별 결제금액, 결제 건수를 나타냅니다. */
export type AnalyticsPgCompanyChartStat = {
	/** 결제대행사 */
	pgCompany: PgCompany
	/**
	 * 결제대행사별 결제금액
	 * (int64)
	 */
	amount: number
	/**
	 * 결제대행사별 결제 건수
	 * (int64)
	 */
	count: number
}

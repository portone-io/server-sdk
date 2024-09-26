import type { PgCompany } from "#generated/common/PgCompany"

/** 특정 시점의 결제대행사 별 결제금액, 결제 건수를 나타냅니다. */
export type AnalyticsPgCompanyTrendChartStat = {
	/**
	 * 시점
	 * (RFC 3339 date-time)
	 */
	timestamp: string
	/** 결제대행사 */
	pgCompany: PgCompany
	/**
	 * 결제금액
	 * (int64)
	 */
	amount: number
	/**
	 * 결제 건수
	 * (int64)
	 */
	count: number
}

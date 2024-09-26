import type { EasyPayProvider } from "#generated/common/EasyPayProvider"

/** 특정 시점의 간편결제사별 결제금액, 결제 건수를 나타냅니다. */
export type AnalyticsEasyPayProviderChartStat = {
	/**
	 * 시점
	 * (RFC 3339 date-time)
	 */
	timestamp: string
	/** 간편결제사 */
	easyPayProvider: EasyPayProvider
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

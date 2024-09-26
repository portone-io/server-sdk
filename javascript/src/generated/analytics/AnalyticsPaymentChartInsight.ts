import type { DayOfWeek } from "#generated/common/DayOfWeek"

/** 고객사의 결제 현황 인사이트 정보 */
export type AnalyticsPaymentChartInsight = {
	/**
	 * 월간 최고 거래액 발생일
	 * (int64)
	 */
	highestDateInMonth?: number
	/**
	 * 월간 최저 거래액 발생일
	 * (int64)
	 */
	lowestDateInMonth?: number
	/** 주간 최고 거래액 발생 요일 */
	highestDayInWeek?: DayOfWeek
	/** 주간 최저 거래액 발생 요일 */
	lowestDayInWeek?: DayOfWeek
	/**
	 * 일간 최고 거래액 발생 시간
	 * (int64)
	 */
	highestHourInDay: number
	/**
	 * 일간 최저 거래액 발생 시간
	 * (int64)
	 */
	lowestHourInDay: number
}

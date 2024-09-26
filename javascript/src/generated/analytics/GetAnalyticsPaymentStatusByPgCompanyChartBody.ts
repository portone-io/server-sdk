import type { Currency } from "#generated/common/Currency"

/** 고객사의 PG사별 결제전환율 조회를 위한 입력 정보 */
export type GetAnalyticsPaymentStatusByPgCompanyChartBody = {
	/**
	 * 조회할 결제 현황의 시작 시간
	 * (RFC 3339 date-time)
	 */
	from: string
	/**
	 * 조회할 결제 현황의 끝 시간
	 * (RFC 3339 date-time)
	 */
	until: string
	/**
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 */
	currency: Currency
}

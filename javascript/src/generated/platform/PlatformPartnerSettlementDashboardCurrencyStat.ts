import type { Currency } from "#generated/common/Currency"
import type { PlatformPartnerSettlementStatusStats } from "#generated/platform/partnerSettlement/PlatformPartnerSettlementStatusStats"

/** 정산 통화별 정산내역 통계 */
export type PlatformPartnerSettlementDashboardCurrencyStat = {
	/** 정산 통화 */
	currency: Currency
	/**
	 * 총 정산 금액
	 * (int64)
	 */
	settlementAmount: number
	/**
	 * 총 주문 금액
	 * (int64)
	 */
	orderAmount: number
	/**
	 * 총 정산 수수료 금액
	 *
	 * 중개 수수료, 중개 수수료 부가세, 추가 수수료, 추가 수수료 부가세, 할인 분담금, 결제금액 부가세 부담금을 더한 금액 입니다.
	 * (int64)
	 */
	feeAmount: number
	/**
	 * 총 수기 정산 금액
	 * (int64)
	 */
	manualAmount: number
	/** 상태별 총 정산 금액 */
	statusSettlementAmount: PlatformPartnerSettlementStatusStats
}

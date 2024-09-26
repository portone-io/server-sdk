import type { Currency } from "#generated/common/Currency"
import type { PromotionCardCompany } from "#generated/promotion/PromotionCardCompany"
import type { PromotionDiscount } from "#generated/promotion/PromotionDiscount"
import type { PromotionStatus } from "#generated/promotion/PromotionStatus"

/** 카드 프로모션 */
export type CardPromotion = {
	/** 프로모션 유형 */
	type: "CARD"
	/** 프로모션 아이디 */
	id: string
	/** 상점 아이디 */
	storeId: string
	/** 프로모션 이름 */
	name: string
	/** 할인 유형 */
	discountType: PromotionDiscount
	/**
	 * 총 예산
	 * (int64)
	 */
	totalBudget: number
	/**
	 * 최소 결제 금액
	 * (int64)
	 */
	minPaymentAmount?: number
	/**
	 * 최대 할인 금액
	 * (int64)
	 */
	maxDiscountAmount?: number
	/**
	 * 소진 금액
	 * (int64)
	 */
	spentAmount: number
	/** 금액 화폐 */
	currency: Currency
	/**
	 * 프로모션 시작 시각
	 * (RFC 3339 date-time)
	 */
	startAt: string
	/**
	 * 프로모션 종료 시각
	 * (RFC 3339 date-time)
	 */
	endAt: string
	/**
	 * 프로모션 중단 시각
	 * (RFC 3339 date-time)
	 */
	terminatedAt?: string
	/** 프로모션 카드사 */
	cardCompany: PromotionCardCompany
	/** 프로모션 상태 */
	status: PromotionStatus
	/**
	 * 프로모션 생성 시각
	 * (RFC 3339 date-time)
	 */
	createdAt: string
}

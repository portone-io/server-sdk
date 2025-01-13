import type { Currency } from "./../../common/Currency"
import type { PromotionCardCompany } from "./../../payment/promotion/PromotionCardCompany"
import type { PromotionDiscountPolicy } from "./../../payment/promotion/PromotionDiscountPolicy"
import type { PromotionRecoverOption } from "./../../payment/promotion/PromotionRecoverOption"
import type { PromotionStatus } from "./../../payment/promotion/PromotionStatus"
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
	/** 할인 정책 */
	discountPolicy: PromotionDiscountPolicy
	/**
	 * 총 예산
	 * (int64)
	 */
	totalBudget: number
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
	/** 결제 취소 시 프로모션 예산 복구 옵션 */
	recoverOption: PromotionRecoverOption
}

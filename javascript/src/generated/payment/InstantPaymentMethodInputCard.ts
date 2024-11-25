import type { CardCredential } from "./../common/CardCredential"
/** 카드 수단 정보 입력 정보 */
export type InstantPaymentMethodInputCard = {
	/** 카드 인증 관련 정보 */
	credential: CardCredential
	/**
	 * 카드 할부 개월 수
	 * (int32)
	 */
	installmentMonth?: number
	/** 무이자 할부 적용 여부 */
	useFreeInstallmentPlan?: boolean
	/** 무이자 할부 이자를 고객사가 부담할지 여부 */
	useFreeInterestFromMerchant?: boolean
	/** 카드 포인트 사용 여부 */
	useCardPoint?: boolean
}

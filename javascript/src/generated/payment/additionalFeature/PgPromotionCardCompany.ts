/**
 * PG 프로모션 카드사
 *
 * PG사 프로모션 조회 시 필터링할 수 있는 카드사 목록입니다.
 */
export type PgPromotionCardCompany =
	/** KDB산업은행 */
	| "KOREA_DEVELOPMENT_BANK"
	/** 새마을금고 */
	| "KFCC"
	/** 신협 */
	| "SHINHYUP"
	/** 우체국 */
	| "EPOST"
	/** 저축은행 */
	| "SAVINGS_BANK_KOREA"
	/** 카카오뱅크 */
	| "KAKAO_BANK"
	/** 우리카드 */
	| "WOORI_CARD"
	/** BC카드 */
	| "BC_CARD"
	/** 광주카드 */
	| "GWANGJU_CARD"
	/** 삼성카드 */
	| "SAMSUNG_CARD"
	/** 신한카드 */
	| "SHINHAN_CARD"
	/** 현대카드 */
	| "HYUNDAI_CARD"
	/** 롯데카드 */
	| "LOTTE_CARD"
	/** 수협카드 */
	| "SUHYUP_CARD"
	/** 씨티카드 */
	| "CITI_CARD"
	/** NH카드 */
	| "NH_CARD"
	/** 전북카드 */
	| "JEONBUK_CARD"
	/** 제주카드 */
	| "JEJU_CARD"
	/** 하나카드 */
	| "HANA_CARD"
	/** 국민카드 */
	| "KOOKMIN_CARD"
	/** 케이뱅크 */
	| "K_BANK"
	/** 토스뱅크 */
	| "TOSS_BANK"
	/** 미래에셋증권 */
	| "MIRAE_ASSET_SECURITIES"
	| string & {}

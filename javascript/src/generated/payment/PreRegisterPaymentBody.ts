import type { Currency } from "./../common/Currency"
/** 결제 정보 사전 등록 입력 정보 */
export type PreRegisterPaymentBody = {
	/**
	 * 상점 아이디
	 *
	 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
	 */
	storeId?: string
	/**
	 * 결제 총 금액
	 * (int64)
	 */
	totalAmount?: number
	/**
	 * 결제 면세 금액
	 * (int64)
	 */
	taxFreeAmount?: number
	/** 통화 단위 */
	currency?: Currency
}

import type { Currency } from "./../common/Currency"
/** 결제 승인 입력 정보 */
export type ConfirmPaymentBody = {
	/**
	 * 상점 아이디
	 *
	 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
	 */
	storeId?: string
	/**
	 * 결제 토큰
	 *
	 * 인증 완료 시 발급된 토큰입니다.
	 */
	paymentToken: string
	/**
	 * 결제 시도 아이디
	 *
	 * 검증용 파라미터로, 결제 시도 아이디와 일치하지 않을 경우 오류가 반환됩니다.
	 */
	txId?: string
	/**
	 * 통화
	 *
	 * 검증용 파라미터로, 결제 건 화폐와 일치하지 않을 경우 오류가 반환됩니다. 값 전달을 권장합니다.
	 */
	currency?: Currency
	/**
	 * 결제 금액
	 *
	 * 검증용 파라미터로, 결제 건 총 금액과 일치하지 않을 경우 오류가 반환됩니다. 값 전달을 권장합니다.
	 * (int64)
	 */
	totalAmount?: number
	/**
	 * 면세 금액
	 *
	 * 검증용 파라미터로, 결제 건 면세 금액과 일치하지 않을 경우 오류가 반환됩니다.
	 * (int64)
	 */
	taxFreeAmount?: number
	/**
	 * 테스트 결제 여부
	 *
	 * 검증용 파라미터로, 결제 건 테스트 여부와 일치하지 않을 경우 오류가 반환됩니다. 값 전달을 권장합니다.
	 */
	isTest?: boolean
}

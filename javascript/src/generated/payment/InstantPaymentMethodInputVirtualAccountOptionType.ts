/** 가상계좌 발급 유형 */
export type InstantPaymentMethodInputVirtualAccountOptionType =
	/**
	 * 회전식 가상계좌
	 *
	 * 일반적으로 사용되는 방식이며 PG사에서 직접 채번한 가상계좌번호를 사용합니다.
	 */
	| "NORMAL"
	/** 고정식 가상계좌 */
	| "FIXED"

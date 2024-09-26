/**
 * 입금 만료 기한
 *
 * validHours와 dueDate 둘 중 하나의 필드만 입력합니다.
 */
export type InstantPaymentMethodInputVirtualAccountExpiry = {
	/**
	 * 유효 시간
	 *
	 * 시간 단위로 입력합니다.
	 * (int32)
	 */
	validHours?: number
	/**
	 * 만료 시점
	 * (RFC 3339 date-time)
	 */
	dueDate?: string
}

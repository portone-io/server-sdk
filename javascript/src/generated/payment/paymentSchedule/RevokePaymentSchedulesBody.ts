/** 결제 예약 건 취소 요청 입력 정보 */
export type RevokePaymentSchedulesBody = {
	/**
	 * 상점 아이디
	 *
	 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
	 */
	storeId?: string
	/** 빌링키 */
	billingKey?: string
	/** 결제 예약 건 아이디 목록 */
	scheduleIds?: string[]
}

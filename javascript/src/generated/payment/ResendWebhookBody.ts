/** 웹훅 재발송을 위한 입력 정보 */
export type ResendWebhookBody = {
	/**
	 * 상점 아이디
	 *
	 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
	 */
	storeId?: string
	/**
	 * 웹훅 아이디
	 *
	 * 입력하지 않으면 결제 건의 가장 최근 웹훅 아이디가 기본 적용됩니다
	 */
	webhookId?: string
}
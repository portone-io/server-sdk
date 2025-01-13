/** 플랫폼 설정 업데이트를 위한 입력 정보 */
export type UpdatePlatformSettingBody = {
	/** 기본 보내는 이 통장 메모 */
	defaultWithdrawalMemo?: string
	/** 기본 받는 이 통장 메모 */
	defaultDepositMemo?: string
}

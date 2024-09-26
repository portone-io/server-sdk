/** 예금주 조회 성공 응답 정보 */
export type PlatformAccountHolder = {
	/** 계좌 예금주 이름 */
	holderName: string
	/** 계좌 검증 아이디 */
	accountVerificationId: string
}

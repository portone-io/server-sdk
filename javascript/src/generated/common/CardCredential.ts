/** 카드 인증 관련 정보 */
export type CardCredential = {
	/** 카드 번호 (숫자만) */
	number: string
	/** 유효 기간 만료 연도 (2자리) */
	expiryYear: string
	/** 유효 기간 만료 월 (2자리) */
	expiryMonth: string
	/** 생년월일 (yyMMdd) 또는 사업자 등록 번호 (10자리, 숫자만) */
	birthOrBusinessRegistrationNumber?: string
	/** 비밀번호 앞 2자리 */
	passwordTwoDigits?: string
}

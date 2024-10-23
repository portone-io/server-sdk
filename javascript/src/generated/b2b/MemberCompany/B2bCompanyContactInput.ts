/** 담당자 관련 입력 정보 */
export type B2bCompanyContactInput = {
	/**
	 * 담당자 계정 ID
	 *
	 * 팝빌 로그인 계정으로 사용됩니다.
	 * 값을 입력하지 않을 경우 자동 채번됩니다.
	 */
	loginId?: string
	/**
	 * 비밀번호
	 *
	 * 값을 입력하지 않을 경우 자동 채번됩니다.
	 */
	password?: string
	/** 담당자 성명 */
	name: string
	/** 담당자 핸드폰 번호 */
	phoneNumber: string
	/** 담당자 이메일 */
	email: string
}

export type B2bCompanyContactInput = {
	/**
	 * 담당자 ID
	 *
	 * 팝빌 로그인 계정으로 사용됩니다.
	 */
	id: string
	/** 비밀번호 */
	password: string
	/** 담당자 성명 */
	name: string
	/** 담당자 핸드폰 번호 */
	phoneNumber: string
	/** 담당자 이메일 */
	email: string
}

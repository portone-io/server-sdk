export type B2bCompanyContact = {
	/**
	 * 담당자 ID
	 *
	 * 팝빌 로그인 계정으로 사용됩니다.
	 */
	id: string
	/** 담당자 성명 */
	name: string
	/** 담당자 핸드폰 번호 */
	phoneNumber: string
	/** 담당자 이메일 */
	email: string
	/**
	 * 등록 일시
	 * (RFC 3339 date-time)
	 */
	registeredAt: string
	/**
	 * 관리자 여부
	 *
	 * true일 경우 관리자, false일 경우 담당자입니다.
	 */
	isManager: boolean
}

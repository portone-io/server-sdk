/** 요청 시 고객 정보 */
export type IdentityVerificationRequestedCustomer = {
	/** 식별 아이디 */
	id?: string
	/** 이름 */
	name?: string
	/**
	 * 전화번호
	 *
	 * 특수 문자(-) 없이 숫자로만 이루어진 번호 형식입니다.
	 */
	phoneNumber?: string
	/** 출생연도 */
	birthYear?: string
	/** 출생월 */
	birthMonth?: string
	/** 출생일 */
	birthDay?: string
}

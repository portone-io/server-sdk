/** 본인인증 요청을 위한 고객 정보 */
export type SendIdentityVerificationBodyCustomer = {
	/** 식별 아이디 */
	id?: string
	/** 이름 */
	name: string
	/**
	 * 전화번호
	 *
	 * 특수 문자(-) 없이 숫자만 입력합니다.
	 */
	phoneNumber: string
	/**
	 * 주민등록번호 앞 7자리
	 *
	 * SMS 방식의 경우 필수로 입력합니다.
	 */
	identityNumber?: string
	/**
	 * IP 주소
	 *
	 * 고객의 요청 속도 제한에 사용됩니다.
	 */
	ipAddress: string
}

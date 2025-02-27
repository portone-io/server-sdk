import type { Gender } from "./../common/Gender"
/** 본인인증 다건 조회를 위한 고객 정보 입력 정보 */
export type IdentityVerificationFilterCustomerInput = {
	/** 이름 */
	name?: string
	/** 출생 연도 */
	birthYear?: string
	/** 출생월 */
	birthMonth?: string
	/** 출생일 */
	birthDay?: string
	/**
	 * 전화번호
	 *
	 * 특수 문자(-) 없이 숫자로만 이루어진 번호 형식입니다.
	 */
	phoneNumber?: string
	/** 성별 */
	gender?: Gender
}

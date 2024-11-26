import type { Address } from "./../common/Address"
import type { Gender } from "./../common/Gender"
/** 고객 정보 */
export type Customer = {
	/**
	 * 고객 아이디
	 *
	 * 고객사가 지정한 고객의 고유 식별자입니다.
	 */
	id?: string
	/** 이름 */
	name?: string
	/** 출생 연도 */
	birthYear?: string
	/** 성별 */
	gender?: Gender
	/** 이메일 */
	email?: string
	/** 전화번호 */
	phoneNumber?: string
	/** 주소 */
	address?: Address
	/** 우편번호 */
	zipcode?: string
}

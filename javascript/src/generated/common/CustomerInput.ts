import type { Country } from "./../common/Country"
import type { CustomerNameInput } from "./../common/CustomerNameInput"
import type { Gender } from "./../common/Gender"
import type { SeparatedAddressInput } from "./../common/SeparatedAddressInput"

/** 고객 정보 입력 정보 */
export type CustomerInput = {
	/**
	 * 고객 아이디
	 *
	 * 고객사가 지정한 고객의 고유 식별자입니다.
	 */
	id?: string
	/** 이름 */
	name?: CustomerNameInput
	/** 출생 연도 */
	birthYear?: string
	/** 출생월 */
	birthMonth?: string
	/** 출생일 */
	birthDay?: string
	/** 국가 */
	country?: Country
	/** 성별 */
	gender?: Gender
	/** 이메일 */
	email?: string
	/** 전화번호 */
	phoneNumber?: string
	/** 주소 */
	address?: SeparatedAddressInput
	/** 우편번호 */
	zipcode?: string
	/** 사업자 등록 번호 */
	businessRegistrationNumber?: string
}

import type { Gender } from "./../common/Gender"
import type { IdentityVerificationOperator } from "./../identityVerification/IdentityVerificationOperator"
/** 인증된 고객 정보 */
export type IdentityVerificationVerifiedCustomer = {
	/** 식별 아이디 */
	id?: string
	/** 이름 */
	name: string
	/**
	 * 통신사
	 *
	 * 다날: 별도 계약이 필요합니다.
	 * KG이니시스: 제공하지 않습니다.
	 */
	operator?: IdentityVerificationOperator
	/**
	 * 전화번호
	 *
	 * 특수 문자(-) 없이 숫자로만 이루어진 번호 형식입니다.
	 * 다날: 별도 계약이 필요합니다.
	 * KG이니시스: 항상 제공합니다.
	 */
	phoneNumber?: string
	/**
	 * 생년월일 (yyyy-MM-dd)
	 *
	 * 포트원 V2 본인인증 건의 경우 항상 존재합니다.
	 * (yyyy-MM-dd)
	 */
	birthDate?: string
	/**
	 * 성별
	 *
	 * 다날: 항상 제공합니다.
	 * KG이니시스: 항상 제공합니다.
	 */
	gender?: Gender
	/**
	 * 외국인 여부
	 *
	 * 다날: 별도 계약이 필요합니다.
	 * KG이니시스: 항상 제공합니다.
	 */
	isForeigner?: boolean
	/**
	 * CI (개인 고유 식별키)
	 *
	 * 개인을 식별하기 위한 고유 정보입니다.
	 * 다날: 항상 제공합니다.
	 * KG이니시스: 카카오를 제외한 인증사에서 제공합니다.
	 */
	ci?: string
	/**
	 * DI (사이트별 개인 고유 식별키)
	 *
	 * 중복 가입을 방지하기 위해 개인을 식별하는 사이트별 고유 정보입니다.
	 * 다날: 항상 제공합니다.
	 * KG이니시스: 제공하지 않습니다.
	 */
	di?: string
}

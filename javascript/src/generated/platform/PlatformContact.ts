/**
 * 플랫폼 파트너 담당자 연락 정보
 *
 * 파트너 담당자에게 연락하기 위한 정보들 입니다.
 */
export type PlatformContact = {
	/** 담당자 이름 */
	name: string
	/** 담당자 휴대폰 번호 */
	phoneNumber?: string
	/** 담당자 이메일 */
	email: string
}

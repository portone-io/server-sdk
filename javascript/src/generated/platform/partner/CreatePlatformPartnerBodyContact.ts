/** 파트너 담당자 정보 */
export type CreatePlatformPartnerBodyContact = {
	/** 담당자 이름 */
	name: string
	/** 담당자 휴대폰 번호 */
	phoneNumber?: string
	/** 담당자 이메일 */
	email: string
}

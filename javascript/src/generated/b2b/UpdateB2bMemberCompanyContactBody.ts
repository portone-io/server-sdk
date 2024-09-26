/** 담당자 정보 수정 요청 */
export type UpdateB2bMemberCompanyContactBody = {
	/** 비밀번호 */
	password?: string
	/** 담당자 성명 */
	name?: string
	/** 담당자 핸드폰 번호 */
	phoneNumber?: string
	/** 담당자 이메일 */
	email?: string
}

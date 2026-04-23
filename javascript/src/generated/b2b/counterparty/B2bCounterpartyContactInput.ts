/** 거래처 담당자 입력 정보 */
export type B2bCounterpartyContactInput = {
	/** 담당자 성명 */
	name: string
	/** 담당자 전화번호 */
	phoneNumber?: string
	/** 담당자 이메일 */
	email: string
	/** 담당자 메모 */
	memo?: string
}

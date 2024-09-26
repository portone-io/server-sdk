/** 연동 사업자 정보 수정 요청 */
export type UpdateB2bMemberCompanyBody = {
	/** 회사명 */
	name?: string
	/** 대표자 성명 */
	ceoName?: string
	/** 회사 주소 */
	address?: string
	/** 업태 */
	businessType?: string
	/** 업종 */
	businessClass?: string
}

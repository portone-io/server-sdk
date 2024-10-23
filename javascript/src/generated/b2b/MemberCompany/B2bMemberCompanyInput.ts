/** 사업자 입력 정보 */
export type B2bMemberCompanyInput = {
	/** 사업자등록번호 */
	brn: string
	/** 회사명 */
	companyName: string
	/** 대표자 성명 */
	representativeName: string
	/** 회사 주소 */
	address: string
	/** 업태 */
	businessType: string
	/** 업종 */
	businessClass: string
}

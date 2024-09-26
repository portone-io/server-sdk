export type B2bMemberCompany = {
	/**
	 * 사업자등록번호
	 *
	 * `-` 없이 숫자로만 구성됩니다.
	 */
	brn: string
	/** 회사명 */
	name: string
	/** 대표자 성명 */
	ceoName: string
	/** 회사 주소 */
	address: string
	/** 업태 */
	businessType: string
	/** 업종 */
	businessClass: string
}

/** 사업자등록 정보 */
export type B2bBusinessInfo = {
	/** 사업자등록번호 */
	brn: string
	/** 상호 */
	name: string
	/** 대표자명 */
	ceoName: string
	/** 우편번호 */
	zipCode: string
	/** 주소 */
	address: string
	/** 사업자 유형 */
	businessEntityType: string
	/** 사업 상태 */
	businessStatus: string
	/** 과세 유형 */
	taxationType: string
	/** 간이과세-일반과세 전환일 */
	simplifiedTaxationTypeDate?: string
	/** 폐업일 */
	closingDate?: string
	/** 개업일 */
	openingDate: string
	/** 업태 */
	businessType: string
	/** 종목 */
	businessClass: string
	/** 업종코드 */
	businessCategoryCode: string
	/** 법인등록번호 */
	corpRegNo?: string
	/** 전화번호 */
	phoneNumber?: string
	/** 관할세무서코드 */
	taxOfficeCode?: string
	/** 관할세무서명 */
	taxOfficeName?: string
}

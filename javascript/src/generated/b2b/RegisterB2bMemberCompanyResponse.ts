import type { B2bCompanyContact } from "#generated/b2b/B2bCompanyContact"
import type { B2bMemberCompany } from "#generated/b2b/B2bMemberCompany"

/** 사업자 연동 응답 정보 */
export type RegisterB2bMemberCompanyResponse = {
	/** 사업자 정보 */
	company: B2bMemberCompany
	/** 담당자 정보 */
	contact: B2bCompanyContact
}

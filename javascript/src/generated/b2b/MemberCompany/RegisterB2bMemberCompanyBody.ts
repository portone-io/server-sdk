import type { B2bCompanyContactInput } from "#generated/b2b/MemberCompany/B2bCompanyContactInput"
import type { B2bMemberCompanyInput } from "#generated/b2b/MemberCompany/B2bMemberCompanyInput"

/** 사업자 연동 요청 정보 */
export type RegisterB2bMemberCompanyBody = {
	/** 사업자 정보 */
	company: B2bMemberCompanyInput
	/** 담당자 정보 */
	contact: B2bCompanyContactInput
}

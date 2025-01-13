/** 연동 사업자로 연동된 파트너들을 예약 수정하려고 시도한 경우 */
export type PlatformMemberCompanyConnectedPartnersCannotBeScheduledError = {
	type: "PLATFORM_MEMBER_COMPANY_CONNECTED_PARTNERS_CANNOT_BE_SCHEDULED"
	ids: string[]
	graphqlIds: string[]
	message?: string
}

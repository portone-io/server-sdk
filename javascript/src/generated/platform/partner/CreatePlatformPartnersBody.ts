import type { CreatePlatformPartnerBody } from "#generated/platform/partner/CreatePlatformPartnerBody"

/** 파트너 다건 생성을 위한 입력 정보 */
export type CreatePlatformPartnersBody = {
	/** 생성할 파트너 리스트 정보 */
	partners: CreatePlatformPartnerBody[]
}

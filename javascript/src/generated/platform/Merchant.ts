import type { Analytics } from "#generated/platform/Analytics"

/** 고객사 정보 */
export type Merchant = {
	/** 고객사 아이디 */
	id: string
	graphqlId: string
	/** 리포트 정보 */
	analytics: Analytics
}

import type { PgCompany } from "#generated/common/PgCompany"

/** 채널 */
export type PlatformPaymentChannel = {
	/** 채널 아이디 */
	id: string
	/** 채널 키 */
	key: string
	/** 채널 이름 */
	name: string
	/** PG사 가맹점 식별 아이디 */
	pgMerchantId: string
	/** PG사 */
	pgCompany?: PgCompany
}

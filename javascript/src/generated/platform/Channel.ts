import type { ChannelType } from "#generated/platform/ChannelType"
import type { PgCompany } from "#generated/common/PgCompany"
import type { PgProvider } from "#generated/common/PgProvider"

/** 채널 정보 */
export type Channel = {
	/** 채널 아이디 */
	id: string
	/** 채널명 */
	name: string
	/** PG사 모듈 */
	pgProvider: PgProvider
	/** PG사 모듈에 해당하는 PG사 */
	pgCompany: PgCompany
	/** 채널 유형 */
	type: ChannelType
	/** PG사 상점 아이디 */
	pgMerchantId: string
	/** 결제용 채널 여부 */
	isForPayment: boolean
	/** 본인인증용 채널 여부 */
	isForIdentityVerification: boolean
	/** 채널 키 */
	key: string
}

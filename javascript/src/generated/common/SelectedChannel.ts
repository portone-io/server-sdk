import type { PgProvider } from "./../common/PgProvider"
import type { SelectedChannelType } from "./../common/SelectedChannelType"
/** (결제, 본인인증 등에) 선택된 채널 정보 */
export type SelectedChannel = {
	/** 채널 타입 */
	type: SelectedChannelType
	/** 채널 아이디 */
	id?: string
	/** 채널 키 */
	key?: string
	/** 채널 명 */
	name?: string
	/** PG사 결제 모듈 */
	pgProvider: PgProvider
	/** PG사 고객사 식별 아이디 */
	pgMerchantId: string
}

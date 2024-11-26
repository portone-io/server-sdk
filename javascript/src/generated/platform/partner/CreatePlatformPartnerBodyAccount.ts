import type { Bank } from "./../../common/Bank"
import type { Currency } from "./../../common/Currency"
/** 파트너 계좌 등록을 위한 정보 */
export type CreatePlatformPartnerBodyAccount = {
	/** 은행 */
	bank: Bank
	/** 정산에 사용할 통화 */
	currency: Currency
	/** 계좌번호 */
	number: string
	/** 예금주명 */
	holder: string
	/** 계좌 검증 아이디 */
	accountVerificationId?: string
}

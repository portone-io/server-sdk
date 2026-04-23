import type { Bank } from "./../../common/Bank"
import type { PlatformBankAccountProvider } from "./../../platform/accountTransfer/PlatformBankAccountProvider"
/** 계좌 상세 정보 */
export type PlatformBankAccountDetail = {
	/** 계좌번호 */
	accountNumber: string
	/** 은행 */
	bank: Bank
	/** 제공자 */
	provider: PlatformBankAccountProvider
	/** 예금주명 */
	holder?: string
}

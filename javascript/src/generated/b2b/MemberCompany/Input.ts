import type { Bank } from "#generated/common/Bank"

export type Input = {
	/** 은행 */
	bank: Bank
	/** 계좌번호 */
	accountNumber: string
}

import type { Currency } from "#generated/common/Currency"

export type PlatformDepositAccountTransfer = {
	/** 계좌 이체 유형 */
	type: "DEPOSIT"
	/** 계좌 이체 아이디 */
	id: string
	/** 통화 */
	currency: Currency
	/**
	 * 금액
	 * (int64)
	 */
	amount: number
	/** 입금 계좌 적요 */
	depositMemo?: string
	isForTest: boolean
	/**
	 * 생성 일자
	 * (RFC 3339 date-time)
	 */
	createdAt: string
	/**
	 * 수정 일자
	 * (RFC 3339 date-time)
	 */
	updatedAt: string
	/** 입금자명 */
	depositorName: string
}

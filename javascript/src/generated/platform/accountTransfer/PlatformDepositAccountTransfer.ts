import type { Currency } from "./../../common/Currency"
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
	/**
	 * 이체 일시
	 * (RFC 3339 date-time)
	 */
	tradedAt?: string
	/**
	 * 생성 일시
	 * (RFC 3339 date-time)
	 */
	createdAt: string
	/**
	 * 수정 일시
	 * (RFC 3339 date-time)
	 */
	updatedAt: string
	/** 입금자명 */
	depositorName: string
	/** 테스트 모드 여부 */
	isForTest: boolean
}

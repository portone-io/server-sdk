import type { Bank } from "#generated/common/Bank"
import type { Currency } from "#generated/common/Currency"

export type PlatformPartnerPayoutAccountTransfer = {
	/** 계좌 이체 유형 */
	type: "PARTNER_PAYOUT"
	/** 계좌 이체 아이디 */
	id: string
	/**
	 * 거래 일련번호
	 * (int32)
	 */
	sequenceNumber: number
	/** 통화 */
	currency: Currency
	/** 입금 계좌 은행 */
	depositBank: Bank
	/** 입금 계좌 번호 */
	depositAccountNumber: string
	/**
	 * 금액
	 * (int64)
	 */
	amount: number
	/** 출금 계좌 적요 */
	withdrawalMemo?: string
	/** 입금 계좌 적요 */
	depositMemo?: string
	/**
	 * 잔액
	 * (int64)
	 */
	balance?: number
	/** 실패 사유 */
	failReason?: string
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
	/** 파트너 고유 아이디 */
	partnerId: string
	partnerGraphqlId: string
	/** 일괄 지급 고유 아이디 */
	bulkPayoutId: string
	bulkPayoutGraphqlId: string
	/** 지급 고유 아이디 */
	payoutId: string
	payoutGraphqlId: string
}

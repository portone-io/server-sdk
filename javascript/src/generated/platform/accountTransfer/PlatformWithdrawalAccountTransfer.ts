import type { Bank } from "./../../common/Bank"
import type { Currency } from "./../../common/Currency"
import type { PlatformAccountTransferStatus } from "./../../platform/accountTransfer/PlatformAccountTransferStatus"
import type { Type } from "./../../platform/accountTransfer/Type"
export type PlatformWithdrawalAccountTransfer = {
	/** 계좌 이체 유형 */
	type: "WITHDRAWAL"
	/** 계좌 이체 아이디 */
	id: string
	/** 출금 계좌 아이디 */
	bankAccountId: string
	bankAccountGraphqlId: string
	/**
	 * 거래 일련번호
	 * (int32)
	 */
	sequenceNumber?: number
	/** 통화 */
	currency: Currency
	/** 이체 계좌 은행 */
	depositBank: Bank
	/** 이체 계좌 번호 */
	depositAccountNumber: string
	/** 예금주 */
	depositAccountHolder: string
	/**
	 * 금액
	 * (int64)
	 */
	amount: number
	/** 보내는 이 통장 메모 */
	withdrawalMemo?: string
	/** 받는 이 통장 메모 */
	depositMemo?: string
	/**
	 * 잔액
	 * (int64)
	 */
	balance?: number
	/** 실패 사유 */
	failReason?: string
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
	/** 테스트 모드 여부 */
	isForTest: boolean
	/** 출금 유형 */
	withdrawalType: Type
	/** 파트너 고유 아이디 */
	partnerId?: string
	partnerGraphqlId?: string
	/** 일괄 지급 고유 아이디 */
	bulkPayoutId?: string
	bulkPayoutGraphqlId?: string
	/** 지급 고유 아이디 */
	payoutId?: string
	payoutGraphqlId?: string
	bulkAccountTransferId?: string
	bulkAccountTransferGraphqlId?: string
	/** 전자서명 아이디 */
	documentId?: string
	/**
	 * 상태 업데이트 일시
	 * (RFC 3339 date-time)
	 */
	statusUpdatedAt: string
	/** 상태 */
	status: PlatformAccountTransferStatus
	/**
	 * 예정 일시
	 * (RFC 3339 date-time)
	 */
	scheduledAt?: string
}

import type { PlatformDepositAccountTransfer } from "#generated/platform/accountTransfer/PlatformDepositAccountTransfer"
import type { PlatformPartnerPayoutAccountTransfer } from "#generated/platform/accountTransfer/PlatformPartnerPayoutAccountTransfer"
import type { PlatformRemitAccountTransfer } from "#generated/platform/accountTransfer/PlatformRemitAccountTransfer"

/**
 * 계좌 이체
 *
 * 송금 대행을 통해 일어난 정산 금액 지급, 인출 목적의 계좌 이체 결과 정보입니다.
 */
export type PlatformAccountTransfer =
	| PlatformDepositAccountTransfer
	| PlatformPartnerPayoutAccountTransfer
	| PlatformRemitAccountTransfer

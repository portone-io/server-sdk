import type { PlatformDepositAccountTransfer } from "./../../platform/accountTransfer/PlatformDepositAccountTransfer"
import type { PlatformPartnerPayoutAccountTransfer } from "./../../platform/accountTransfer/PlatformPartnerPayoutAccountTransfer"
import type { PlatformRemitAccountTransfer } from "./../../platform/accountTransfer/PlatformRemitAccountTransfer"

/**
 * 계좌 이체
 *
 * 송금 대행을 통해 일어난 정산 금액 지급, 인출 목적의 계좌 이체 결과 정보입니다.
 */
export type PlatformAccountTransfer =
	| PlatformDepositAccountTransfer
	| PlatformPartnerPayoutAccountTransfer
	| PlatformRemitAccountTransfer
	| { readonly type: unique symbol }

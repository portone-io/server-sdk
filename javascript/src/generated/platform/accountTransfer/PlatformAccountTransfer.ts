import type { Unrecognized } from "./../../../utils/unrecognized"
import type { PlatformDepositAccountTransfer } from "./../../platform/accountTransfer/PlatformDepositAccountTransfer"
import type { PlatformWithdrawalAccountTransfer } from "./../../platform/accountTransfer/PlatformWithdrawalAccountTransfer"
/**
 * 계좌 이체
 *
 * 송금 대행을 통해 일어난 정산 금액 지급, 인출 목적의 계좌 이체 결과 정보입니다.
 */
export type PlatformAccountTransfer =
	| PlatformDepositAccountTransfer
	| PlatformWithdrawalAccountTransfer
	| { readonly type: Unrecognized }

export function isUnrecognizedPlatformAccountTransfer(entity: PlatformAccountTransfer): entity is { readonly type: Unrecognized } {
	return entity.type !== "DEPOSIT"
		&& entity.type !== "WITHDRAWAL"
}

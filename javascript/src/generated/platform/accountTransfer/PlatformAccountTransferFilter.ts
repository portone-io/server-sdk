import type { PlatformAccountTransferType } from "./../../platform/accountTransfer/PlatformAccountTransferType"

export type PlatformAccountTransferFilter = {
	/** 계좌 이체 유형 */
	types?: PlatformAccountTransferType[]
}

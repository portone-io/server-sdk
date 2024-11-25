import type { PlatformContract } from "./../../platform/PlatformContract"
/** 계약 보관 성공 응답 */
export type ArchivePlatformContractResponse = {
	/** 보관된 계약 */
	contract: PlatformContract
}

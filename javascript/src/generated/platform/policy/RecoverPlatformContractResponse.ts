import type { PlatformContract } from "./../../platform/PlatformContract"
/** 계약 복원 성공 응답 */
export type RecoverPlatformContractResponse = {
	/** 복원된 계약 */
	contract: PlatformContract
}

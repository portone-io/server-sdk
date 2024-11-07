import type { PlatformContract } from "./../../platform/PlatformContract"

/** 계약 객체 업데이트 성공 응답 */
export type UpdatePlatformContractResponse = {
	/** 업데이트된 계약 객체 */
	contract: PlatformContract
}

import type { PlatformContract } from "#generated/platform/PlatformContract"

/** 계약 객체 생성 성공 응답 */
export type CreatePlatformContractResponse = {
	/** 생성된 계약 객체 */
	contract: PlatformContract
}

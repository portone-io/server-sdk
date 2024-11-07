import type { PageInput } from "./../../common/PageInput"
import type { PlatformAdditionalFeePolicyFilterInput } from "./../../platform/policy/PlatformAdditionalFeePolicyFilterInput"

/** 추가 수수료 정책 다건 조회를 위한 입력 정보 */
export type GetPlatformAdditionalFeePoliciesBody = {
	/** 요청할 페이지 정보 */
	page?: PageInput
	/** 조회할 추가 수수료 정책 조건 필터 */
	filter?: PlatformAdditionalFeePolicyFilterInput
}

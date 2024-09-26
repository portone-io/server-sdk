import type { PageInput } from "#generated/common/PageInput"
import type { PlatformDiscountSharePolicyFilterInput } from "#generated/platform/policy/PlatformDiscountSharePolicyFilterInput"

/** 할인 분담 정책 다건 조회를 위한 입력 정보 */
export type GetPlatformDiscountSharePoliciesBody = {
	/** 요청할 페이지 정보 */
	page?: PageInput
	/** 조회할 할인 분담 정책 조건 필터 */
	filter?: PlatformDiscountSharePolicyFilterInput
}

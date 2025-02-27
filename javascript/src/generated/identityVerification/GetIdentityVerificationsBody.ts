import type { IdentityVerificationFilterInput } from "./../identityVerification/IdentityVerificationFilterInput"
import type { IdentityVerificationSortInput } from "./../identityVerification/IdentityVerificationSortInput"
import type { PageInput } from "./../common/PageInput"
/** 본인인증 내역 다건 조회를 위한 입력 정보 */
export type GetIdentityVerificationsBody = {
	/**
	 * 요청할 페이지 정보
	 *
	 * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
	 */
	page?: PageInput
	/**
	 * 정렬 조건
	 *
	 * 미 입력 시 sortBy: REQUESTED_AT, sortOrder: DESC 으로 기본값이 적용됩니다.
	 */
	sort?: IdentityVerificationSortInput
	/** 조회할 본인인증 내역 조건 필터 */
	filter?: IdentityVerificationFilterInput
}

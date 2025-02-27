import type { IdentityVerification } from "./../identityVerification/IdentityVerification"
import type { PageInfo } from "./../common/PageInfo"
/** 본인인증 내역 다건 조회 성공 응답 정보 */
export type GetIdentityVerificationsResponse = {
	/** 조회된 본인인증 내역 리스트 */
	items: IdentityVerification[]
	/** 조회된 페이지 정보 */
	page: PageInfo
}

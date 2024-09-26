import type { IdentityVerificationMethod } from "#generated/identityVerification/IdentityVerificationMethod"
import type { IdentityVerificationOperator } from "#generated/identityVerification/IdentityVerificationOperator"
import type { SendIdentityVerificationBodyCustomer } from "#generated/identityVerification/SendIdentityVerificationBodyCustomer"

/** 본인인증 요청을 위한 입력 정보 */
export type SendIdentityVerificationBody = {
	/**
	 * 상점 아이디
	 *
	 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
	 */
	storeId?: string
	/** 채널 키 */
	channelKey: string
	/** 고객 정보 */
	customer: SendIdentityVerificationBodyCustomer
	/** 사용자 지정 데이터 */
	customData?: string
	/** PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고) */
	bypass?: object
	/** 통신사 */
	operator: IdentityVerificationOperator
	/** 본인인증 방식 */
	method: IdentityVerificationMethod
}

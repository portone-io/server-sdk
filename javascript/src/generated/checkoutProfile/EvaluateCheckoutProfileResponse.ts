import type { EvaluatedCheckoutMethod } from "./../checkoutProfile/EvaluatedCheckoutMethod"
/** 체크아웃 프로필 평가 성공 응답 */
export type EvaluateCheckoutProfileResponse = {
	/** 사용 가능한 결제수단 목록 */
	methods?: EvaluatedCheckoutMethod[]
}

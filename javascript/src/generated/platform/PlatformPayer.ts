/**
 * 금액 부담 주체
 *
 * 플랫폼에서 발생한 결제 수수료, 부가세 등 금액을 부담하는 주체를 나타냅니다.
 */
export type PlatformPayer =
	/** 파트너가 부담하는 경우 */
	| "PARTNER"
	/** 고객사가 부담하는 경우 */
	| "MERCHANT"
	| string & {}

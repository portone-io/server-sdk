import type { PaymentOriginPlatformType } from "./../payment/PaymentOriginPlatformType"
/** 결제 출처 정보 */
export type PaymentOrigin = {
	/** 결제를 요청한 플랫폼 타입 */
	platformType: PaymentOriginPlatformType
	/** 결제를 요청한 user agent 문자열 */
	userAgent?: string
	/** 결제를 요청한 페이지 URL */
	url?: string
	/** 결제를 요청한 IP 주소 */
	ipAddress: string
}

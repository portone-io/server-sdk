import type { Carrier } from "#generated/platform/Carrier"

/** 모바일 결제 */
export type ReconciliationPaymentMethodMobile = {
	/** 대사용 결제 수단 */
	type: "MOBILE"
	/** 통신사 */
	carrier?: Carrier
}

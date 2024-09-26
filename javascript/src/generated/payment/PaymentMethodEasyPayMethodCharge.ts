import type { Bank } from "#generated/common/Bank"

/** 충전식 포인트 결제 정보 */
export type PaymentMethodEasyPayMethodCharge = {
	type: "PaymentMethodEasyPayMethodCharge"
	/** 표준 은행 코드 */
	bank?: Bank
}

import type { Card } from "./../../common/Card"
/** 카드 정보 */
export type BillingKeyPaymentMethodCard = {
	type: "BillingKeyPaymentMethodCard"
	/** 카드 상세 정보 */
	card?: Card
}

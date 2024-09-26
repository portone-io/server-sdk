import type { CardCompany } from "#generated/analytics/CardCompany"

/** 카드 결제 */
export type ReconciliationPaymentMethodCard = {
	/** 대사용 결제 수단 */
	type: "CARD"
	/** 카드 발급사 */
	issuer?: CardCompany
	/** 카드 매입사 */
	acquirer?: CardCompany
	/** 카드 승인 번호 */
	approvalNumber?: string
	/**
	 * 카드 할부 개월 수
	 * (int32)
	 */
	installmentMonth?: number
}

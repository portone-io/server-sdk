import type { Card } from "./../common/Card"
import type { PaymentInstallment } from "./../payment/PaymentInstallment"
/** 결제수단 카드 정보 */
export type PaymentMethodCard = {
	type: "PaymentMethodCard"
	/** 카드 상세 정보 */
	card?: Card
	/** 승인 번호 */
	approvalNumber?: string
	/** 할부 정보 */
	installment?: PaymentInstallment
	/** 카드 포인트 사용여부 */
	pointUsed?: boolean
}

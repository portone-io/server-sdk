import type { Bank } from "./../common/Bank"
import type { PaymentMethodVirtualAccountRefundStatus } from "./../payment/PaymentMethodVirtualAccountRefundStatus"
import type { PaymentMethodVirtualAccountType } from "./../payment/PaymentMethodVirtualAccountType"
/** 가상계좌 상세 정보 */
export type PaymentMethodVirtualAccount = {
	type: "PaymentMethodVirtualAccount"
	/** 표준 은행 코드 */
	bank?: Bank
	/** 계좌번호 */
	accountNumber: string
	/** 계좌 유형 */
	accountType?: PaymentMethodVirtualAccountType
	/** 계좌주 */
	remitteeName?: string
	/** 송금인(입금자) */
	remitterName?: string
	/**
	 * 입금만료시점
	 * (RFC 3339 date-time)
	 */
	expiredAt?: string
	/**
	 * 계좌발급시점
	 * (RFC 3339 date-time)
	 */
	issuedAt?: string
	/** 가상계좌 결제가 환불 단계일 때의 환불 상태 */
	refundStatus?: PaymentMethodVirtualAccountRefundStatus
}

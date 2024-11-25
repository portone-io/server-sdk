import type { Bank } from "./../common/Bank"
/** 고객 정보 입력 형식 */
export type CancelPaymentBodyRefundAccount = {
	/** 은행 */
	bank: Bank
	/** 계좌번호 */
	number: string
	/** 예금주 */
	holderName: string
	/** 예금주 연락처 - 스마트로 가상계좌 결제인 경우에 필요합니다. */
	holderPhoneNumber?: string
}

import type { IssueCashReceiptCustomerInputIdentityNumberType } from "./../../payment/cashReceipt/IssueCashReceiptCustomerInputIdentityNumberType"
/** 현금영수증 발급 시 고객 관련 입력 정보 */
export type IssueCashReceiptCustomerInput = {
	/** 고객 식별값 */
	identityNumber: string
	/**
	 * 고객 식별값 유형
	 *
	 * 갤럭시아머니트리의 경우 필요합니다
	 */
	identityNumberType?: IssueCashReceiptCustomerInputIdentityNumberType
	/** 이름 */
	name?: string
	/** 이메일 */
	email?: string
	/** 전화번호 */
	phoneNumber?: string
}

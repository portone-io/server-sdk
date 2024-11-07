import type { CashReceiptInputType } from "./../common/CashReceiptInputType"

/** 현금영수증 입력 정보 */
export type CashReceiptInput = {
	/** 현금영수증 유형 */
	type: CashReceiptInputType
	/**
	 * 사용자 식별 번호
	 *
	 * 미발행 유형 선택 시 입력하지 않습니다.
	 */
	customerIdentityNumber?: string
}

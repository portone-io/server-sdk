import type { RegisterStoreReceiptBodyItem } from "#generated/payment/RegisterStoreReceiptBodyItem"

/** 영수증 내 하위 상점 거래 등록 정보 */
export type RegisterStoreReceiptBody = {
	/** 하위 상점 거래 목록 */
	items: RegisterStoreReceiptBodyItem[]
	/** 상점 아이디 */
	storeId?: string
}

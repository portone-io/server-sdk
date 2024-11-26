import type { Currency } from "./../common/Currency"
/** 하위 상점 거래 정보 */
export type RegisterStoreReceiptBodyItem = {
	/** 하위 상점 사업자등록번호 */
	storeBusinessRegistrationNumber: string
	/** 하위 상점명 */
	storeName: string
	/**
	 * 결제 총 금액
	 * (int64)
	 */
	totalAmount: number
	/**
	 * 면세액
	 * (int64)
	 */
	taxFreeAmount?: number
	/**
	 * 부가세액
	 * (int64)
	 */
	vatAmount?: number
	/**
	 * 공급가액
	 * (int64)
	 */
	supplyAmount?: number
	/** 통화 */
	currency: Currency
}

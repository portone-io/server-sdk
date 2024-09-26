/** 다운로드 할 시트 컬럼 */
export type PlatformTransferSheetField =
	/**
	 * 과세 유형 또는 소득 유형
	 *
	 * 파트너 유형이 사업자인 경우 과세 유형, 원천징수 대상자인 소득 유형입니다.
	 */
	| "TAXATION_TYPE_OR_INCOME_TYPE"
	/** 할인 분담금 */
	| "SETTLEMENT_DISCOUNT_SHARE_AMOUNT"
	/** 결제 내역 아이디 */
	| "PAYMENT_ID"
	/** 할인 금액 */
	| "SETTLEMENT_DISCOUNT_AMOUNT"
	/** 소득 유형 */
	| "INCOME_TYPE"
	/** 결제 공급가액 */
	| "SETTLEMENT_PAYMENT_SUPPLY_AMOUNT"
	/** 정산 건 상태 */
	| "STATUS"
	/** 면세 할인 분담금 */
	| "SETTLEMENT_DISCOUNT_SHARE_TAX_FREE_AMOUNT"
	/** 주문 금액 */
	| "SETTLEMENT_ORDER_AMOUNT"
	/** 정산 건 아이디 */
	| "TRANSFER_ID"
	/** 파트너 유형 */
	| "PARTNER_TYPE"
	/** 면세 할인 금액 */
	| "SETTLEMENT_DISCOUNT_TAX_FREE_AMOUNT"
	/** 주문 명 */
	| "ORDER_NAME"
	/**
	 * 결제 면세액
	 *
	 * 해당 필드는 deprecated되어 9월까지만 유지되고 이후 삭제될 예정입니다. 대신 SETTLEMENT_PAYMENT_TAX_FREE_AMOUNT 필드를 사용해주세요.
	 */
	| "SETTLEMENT_TAX_FREE_AMOUNT"
	/** 추가 수수료 부가세 */
	| "SETTLEMENT_ADDITIONAL_FEE_VAT_AMOUNT"
	/** 정산 통화 */
	| "SETTLEMENT_CURRENCY"
	/** 파트너 이름 */
	| "PARTNER_NAME"
	/** 중개 수수료 부가세 */
	| "SETTLEMENT_PLATFORM_FEE_VAT_AMOUNT"
	/** 결제 수단 */
	| "PAYMENT_METHOD"
	/** 결제 금액 */
	| "SETTLEMENT_PAYMENT_AMOUNT"
	/** 정산 시작 일 */
	| "SETTLEMENT_START_DATE"
	/** 면세 주문 금액 */
	| "SETTLEMENT_ORDER_TAX_FREE_AMOUNT"
	/** 결제 금액 부가세 부담금 */
	| "SETTLEMENT_PAYMENT_VAT_BURDEN_AMOUNT"
	/** 결제 면세액 */
	| "SETTLEMENT_PAYMENT_TAX_FREE_AMOUNT"
	/** 정산 일 */
	| "SETTLEMENT_DATE"
	/**
	 * 결제 공급가액
	 *
	 * 해당 필드는 deprecated되어 9월까지만 유지되고 이후 삭제될 예정입니다. 대신 SETTLEMENT_PAYMENT_SUPPLY_AMOUNT 필드를 사용해주세요.
	 */
	| "SETTLEMENT_SUPPLY_AMOUNT"
	/** 추가 수수료 */
	| "SETTLEMENT_ADDITIONAL_FEE_AMOUNT"
	/** 결제 금액 부가세 */
	| "SETTLEMENT_PAYMENT_VAT_AMOUNT"
	/** 정산 금액 */
	| "SETTLEMENT_AMOUNT"
	/** 중개 수수료 */
	| "SETTLEMENT_PLATFORM_FEE_AMOUNT"
	/** 과세 유형 */
	| "TAXATION_TYPE"
	/** 정산 구분 */
	| "TYPE"

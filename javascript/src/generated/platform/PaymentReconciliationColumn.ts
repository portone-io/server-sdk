/**
 * 거래대사 엑셀파일 필드
 *
 * 중복으로 필드를 선택 가능합니다
 */
export type PaymentReconciliationColumn =
	/** 정산 통화 필드 */
	| "SETTLEMENT_CURRENCY"
	/** 모바일 결제 통신사 필드 */
	| "PAYMENT_METHOD_MOBILE_CARRIER"
	/** 카드 발급사 필드 */
	| "PAYMENT_METHOD_CARD_ISSUER"
	/** 결제 발생 시간 필드 */
	| "PAYMENT_DATETIME"
	/** 부가세 필드 */
	| "VAT_AMOUNT"
	/** 상품권 타입 필드 */
	| "PAYMENT_METHOD_GIFT_CERTIFICATE_TYPE"
	/** PG사 결제 아이디 필드 */
	| "PG_TX_ID"
	/** 정산금액 필드 */
	| "SETTLEMENT_AMOUNT"
	/** 면세 금액 필드 */
	| "TAX_FREE_AMOUNT"
	/** 카드 매입사 필드 */
	| "PAYMENT_METHOD_CARD_ACQUIRER"
	/** 공급가액 필드 */
	| "SUPPLY_AMOUNT"
	/** 결제 금액 필드 */
	| "PAYMENT_AMOUNT"
	/** 결제 통화 필드 */
	| "PAYMENT_CURRENCY"
	/** 고객사 거래내역 아이디 필드 */
	| "PAYMENT_ID"
	/** 간편결제 수단 필드 */
	| "PAYMENT_METHOD_EASY_PAY_METHOD"
	/** 카드 승인번호 필드 */
	| "PAYMENT_METHOD_CARD_APPROVAL_NUMBER"
	/** 대사용 PG사 가맹점 식별자 필드 */
	| "RECONCILIATION_PG_SPECIFIER"
	/** 거래 상태 필드 */
	| "ACTION_TYPE"
	/** PG 수수료 부가세 필드 */
	| "SETTLEMENT_FEE_VAT"
	/** 계좌이체 승인번호 필드 */
	| "PAYMENT_METHOD_TRANSFER_APPROVAL_NUMBER"
	/** 에스크로건 필드 */
	| "IS_ESCROW"
	/** 거래이상 금액 필드 */
	| "ANOMALY_AMOUNT"
	/** 상품권 승인번호 필드 */
	| "PAYMENT_METHOD_GIFT_CERTIFICATE_APPROVAL_NUMBER"
	/** 포트원 결제 아이디 필드 */
	| "TRANSACTION_ID"
	/** PG 수수료 필드 */
	| "SETTLEMENT_FEE"
	/** 기타결제 수단 이름 필드 */
	| "PAYMENT_METHOD_ETC_NAME"
	/** 거래대사 불일치 필드 */
	| "NOT_MATCHED_REASONS"
	/** 거래대사 상태 필드 */
	| "RECONCILIATION_STATUS"
	/** 결제 수단 필드 */
	| "PAYMENT_METHOD_TYPE"
	/** 계좌이체 은행 필드 */
	| "PAYMENT_METHOD_TRANSFER_BANK"
	/** 할부 개월 수 필드 */
	| "INSTALLMENT_MONTH"
	/** 결제 주문명 필드 */
	| "ORDER_NAME"
	/** 가상계좌 은행 필드 */
	| "PAYMENT_METHOD_VIRTUAL_ACCOUNT_BANK"
	/** 정산일 필드 */
	| "SETTLEMENT_DATE"
	/** 포트원 상점 아이디 필드 */
	| "STORE_ID"
	/** 가상계좌 승인번호 필드 */
	| "PAYMENT_METHOD_VIRTUAL_ACCOUNT_APPROVAL_NUMBER"

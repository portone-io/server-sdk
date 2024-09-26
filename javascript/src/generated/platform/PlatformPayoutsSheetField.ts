/** 다운로드 할 시트 컬럼 */
export type PlatformPayoutsSheetField =
	/** 파트너 아이디 */
	| "PARTNER_ID"
	/** 상태 업데이트 시각 */
	| "STATUS_UPDATED_AT"
	/** 지급 상태 */
	| "STATUS"
	/** 출금 메모 */
	| "WITHDRAWAL_MEMO"
	/** 메모 */
	| "MEMO"
	/** 지급 방식 */
	| "METHOD"
	/** 소득세 */
	| "INCOME_TAX_AMOUNT"
	/** 파트너 유형 */
	| "PARTNER_TYPE"
	/** 지방 소득세 */
	| "LOCAL_INCOME_TAX_AMOUNT"
	/** 지급 통화 */
	| "CURRENCY"
	/** 정산 금액 */
	| "SETTLEMENT_AMOUNT"
	/** 과세 유형 */
	| "TAXATION_TYPE"
	/** 지급 계좌 예금주 */
	| "ACCOUNT_HOLDER"
	/**
	 * 과세 유형 또는 소득 유형
	 *
	 * 파트너 유형이 사업자인 경우 과세 유형, 원천징수 대상자인 소득 유형입니다.
	 */
	| "TAXATION_TYPE_OR_INCOME_TYPE"
	/** 소득 유형 */
	| "INCOME_TYPE"
	/** 지급 생성 시각 */
	| "CREATED_AT"
	/** 지급 아이디 */
	| "PAYOUT_ID"
	/** 파트너 이름 */
	| "PARTNER_NAME"
	/** 지급 계좌 번호 */
	| "ACCOUNT_NUMBER"
	/** 지급 금액 */
	| "AMOUNT"
	/** 지급 계좌 은행 */
	| "ACCOUNT_BANK"
	/** 입금 메모 */
	| "DEPOSIT_MEMO"

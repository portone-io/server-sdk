export type PlatformBulkTaskType =
	/** 정산건 일괄 등록 */
	| "CREATE_TRANSFERS"
	/** 파트너 일괄 등록 */
	| "CREATE_PARTNERS"
	/** 파트너 일괄 국세청 연동 */
	| "CONNECT_MEMBER_COMPANIES"
	/** 파트너 일괄 국세청 연동 해제 */
	| "DISCONNECT_MEMBER_COMPANIES"
	/** 정산 내역서 일괄 발송 */
	| "SEND_PAYOUT_SETTLEMENT_STATEMENTS"
	| string & {}

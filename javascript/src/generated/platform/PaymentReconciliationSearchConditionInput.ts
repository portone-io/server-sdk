/**
 * 거래대사 거래내역 검색용 필드
 *
 * 각 필드 중 하나만 적용 됩니다.
 */
export type PaymentReconciliationSearchConditionInput = {
	/** 고객사 거래 아이디 필드 */
	paymentId?: string
	/** 포트원 결제 아이디 필드 */
	transactionId?: string
	/** PG사 거래 아이디 필드 */
	pgTxId?: string
	/** 주문명 필드 */
	orderName?: string
}

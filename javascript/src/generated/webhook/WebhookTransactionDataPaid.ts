/** 결제(예약 결제 포함)가 승인되었을 때 이벤트의 실제 세부 내용입니다. (모든 결제 수단) */
export type WebhookTransactionDataPaid = {
	/** 고객사에서 채번한 결제 건의 고유 주문 번호입니다. */
	paymentId: string
	/** 포트원에서 채번한 고유 거래 번호입니다. 한 결제 건에 여러 시도가 있을 경우 `transactionId` 가 달라질 수 있습니다. */
	transactionId: string
}

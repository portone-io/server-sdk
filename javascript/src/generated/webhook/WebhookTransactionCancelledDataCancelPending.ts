/** (결제 취소가 비동기로 수행되는 경우) 결제 취소를 요청했을 때 이벤트의 실제 세부 내용입니다. */
export type WebhookTransactionCancelledDataCancelPending = {
	/** 고객사에서 채번한 결제 건의 고유 주문 번호입니다. */
	paymentId: string
	/** 웹훅을 트리거한 상점의 아이디입니다. */
	storeId: string
	/** 포트원에서 채번한 고유 거래 번호입니다. 한 결제 건에 여러 시도가 있을 경우 `transactionId` 가 달라질 수 있습니다. */
	transactionId: string
	/** 포트원에서 채번한 결제건의 취소 고유 번호입니다. */
	cancellationId: string
}

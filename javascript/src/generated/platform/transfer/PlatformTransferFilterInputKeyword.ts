/**
 * 정산건 검색 키워드 입력 정보
 *
 * 검색 키워드 적용을 위한 옵션으로, 명시된 키워드를 포함하는 정산건만 조회합니다. 하나의 하위 필드에만 값을 명시하여 요청합니다.
 */
export type PlatformTransferFilterInputKeyword = {
	/** 해당 값이 포함된 정보를 가진 정산건만 조회합니다. */
	all?: string
	/** 해당 값이랑 일치하는 paymentId 를 가진 정산건만 조회합니다. */
	paymentId?: string
	/** 해당 값이랑 일치하는 transferId 를 가진 정산건만 조회합니다. */
	transferId?: string
	/** 해당 값이 포함된 transferMemo 를 가진 정산건만 조회합니다. */
	transferMemo?: string
	/** 해당 값이랑 일치하는 productId 를 가진 정산건만 조회합니다. */
	productId?: string
	/** 해당 값이랑 일치하는 productName 을 가진 정산건만 조회합니다. */
	productName?: string
	/** 해당 값이랑 일치하는 partnerId 를 가진 정산건만 조회합니다. */
	partnerId?: string
	/** 해당 값이 포함된 partnerName 을 가진 정산건만 조회합니다. */
	partnerName?: string
	/** 해당 값이 포함된 partnerMemo 를 가진 정산건만 조회합니다. */
	partnerMemo?: string
	/** 해당 값이 포함된 partnerSettlementId 를 가진 정산건만 조회합니다. */
	partnerSettlementId?: string
	/** 해당 값과 일치하는 지급건에 연관된 정산건만 조회합니다. */
	payoutId?: string
}

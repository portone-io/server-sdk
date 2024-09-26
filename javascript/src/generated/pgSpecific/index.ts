export type * from "./GetKakaopayPaymentOrderError"
export type * from "./GetKakaopayPaymentOrderResponse"
import type { GetKakaopayPaymentOrderResponse } from "#generated/pgSpecific/GetKakaopayPaymentOrderResponse"

export type Operations = {
	/**
	 * 카카오페이 주문 조회 API
	 *
	 * 주어진 아이디에 대응되는 카카오페이 주문 건을 조회합니다.
	 * 해당 API 사용이 필요한 경우 포트원 기술지원팀으로 문의 주시길 바랍니다.
	 *
	 * @param pgTxId
	 * 카카오페이 주문 번호 (tid)
	 * @param channelKey
	 * 채널 키
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getKakaopayPaymentOrder: (
		/** 카카오페이 주문 번호 (tid) */
		pgTxId: string,
		/** 채널 키 */
		channelKey: string,
	) => Promise<GetKakaopayPaymentOrderResponse>
}

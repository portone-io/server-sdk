import type { GetKakaopayPaymentOrderError } from "..//pgSpecific/GetKakaopayPaymentOrderError"
import type { GetKakaopayPaymentOrderResponse } from "..//pgSpecific/GetKakaopayPaymentOrderResponse"
import * as Errors from "..//errors"
export type { GetKakaopayPaymentOrderResponse } from "./GetKakaopayPaymentOrderResponse"
/** @ignore */
export function PgSpecificClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): PgSpecificClient {
	return {
		getKakaopayPaymentOrder: async (
			pgTxId: string,
			channelKey: string,
		): Promise<GetKakaopayPaymentOrderResponse> => {
			const query = [
				["pgTxId", pgTxId],
				["channelKey", channelKey],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/kakaopay/payment/order?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetKakaopayPaymentOrderError = await response.json()
				switch (errorResponse.type) {
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
	}
}
export type PgSpecificClient = {
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
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getKakaopayPaymentOrder: (
		/** 카카오페이 주문 번호 (tid) */
		pgTxId: string,
		/** 채널 키 */
		channelKey: string,
	) => Promise<GetKakaopayPaymentOrderResponse>
}


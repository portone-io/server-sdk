import * as Errors from "../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../client"
import type { GetKakaopayPaymentOrderResponse } from "../../generated/pgSpecific/GetKakaopayPaymentOrderResponse"
import type { GetKakaopayPaymentOrderError as _InternalGetKakaopayPaymentOrderError } from "../../generated/pgSpecific/GetKakaopayPaymentOrderError"
export function PgSpecificClient(init: PortOneClientInit): PgSpecificClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getKakaopayPaymentOrder: async (
			options: {
				pgTxId: string,
				channelKey: string,
			}
		): Promise<GetKakaopayPaymentOrderResponse> => {
			const {
				pgTxId,
				channelKey,
			} = options
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
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetKakaopayPaymentOrderError = await response.json()
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
	 * @throws {@link GetKakaopayPaymentOrderError}
	 */
	getKakaopayPaymentOrder: (
		options: {
			/** 카카오페이 주문 번호 (tid) */
			pgTxId: string,
			/** 채널 키 */
			channelKey: string,
		}
	) => Promise<GetKakaopayPaymentOrderResponse>
}
export type GetKakaopayPaymentOrderError =
	| Errors.InvalidRequestError
	| Errors.UnauthorizedError
export function isGetKakaopayPaymentOrderError(error: Error): error is GetKakaopayPaymentOrderError {
	return (
		error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.UnauthorizedError
	)
}

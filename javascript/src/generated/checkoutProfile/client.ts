import { CheckoutProfileError } from "./CheckoutProfileError"
import type { Unrecognized } from "./../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../client"
import type { Country } from "../../generated/common/Country"
import type { Currency } from "../../generated/common/Currency"
import type { EvaluateCheckoutProfileResponse } from "../../generated/checkoutProfile/EvaluateCheckoutProfileResponse"
import type { InvalidRequestError } from "../../generated/common/InvalidRequestError"
import type { ProfileSettingsNotFoundError } from "../../generated/checkoutProfile/ProfileSettingsNotFoundError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function CheckoutProfileClient(init: PortOneClientInit): CheckoutProfileClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		evaluateCheckoutProfile: async (
			options: {
				profileKey: string,
				country: Country,
				currency: Currency,
				amount: number,
			}
		): Promise<EvaluateCheckoutProfileResponse> => {
			const {
				profileKey,
				country,
				currency,
				amount,
			} = options
			const query = [
				["profileKey", profileKey],
				["country", country],
				["currency", currency],
				["amount", amount],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/checkout-profiles/evaluate?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new EvaluateCheckoutProfileError(await response.json())
			}
			return response.json()
		},
	}
}
export type CheckoutProfileClient = {
	/**
	 * 체크아웃 프로필에서 결제 수단 목록 조회
	 *
	 * 주어진 금액 및 국가에서 사용 가능한 결제 수단 목록을 반환
	 *
	 * @throws {@link EvaluateCheckoutProfileError}
	 */
	evaluateCheckoutProfile: (
		options: {
			/** 프로필 키 */
			profileKey: string,
			/** 국가 */
			country: Country,
			/** 통화 */
			currency: Currency,
			/**
			 * 결제 금액
			 * (int64)
			 */
			amount: number,
		}
	) => Promise<EvaluateCheckoutProfileResponse>
}
export class EvaluateCheckoutProfileError extends CheckoutProfileError {
	declare readonly data: InvalidRequestError | ProfileSettingsNotFoundError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: InvalidRequestError | ProfileSettingsNotFoundError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, EvaluateCheckoutProfileError.prototype)
		this.name = "EvaluateCheckoutProfileError"
	}
}

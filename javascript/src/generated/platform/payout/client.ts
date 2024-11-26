import { PayoutError } from "./PayoutError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetPlatformPayoutsResponse } from "../../../generated/platform/payout/GetPlatformPayoutsResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformNotEnabledError } from "../../../generated/platform/PlatformNotEnabledError"
import type { PlatformPayoutFilterInput } from "../../../generated/platform/payout/PlatformPayoutFilterInput"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
export function PayoutClient(init: PortOneClientInit): PayoutClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatformPayouts: async (
			options?: {
				isForTest?: boolean,
				page?: PageInput,
				filter?: PlatformPayoutFilterInput,
			}
		): Promise<GetPlatformPayoutsResponse> => {
			const isForTest = options?.isForTest
			const page = options?.page
			const filter = options?.filter
			const requestBody = JSON.stringify({
				isForTest,
				page,
				filter,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/payouts?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformPayoutsError(await response.json())
			}
			return response.json()
		},
	}
}
export type PayoutClient = {
	/**
	 * 지급 내역 다건 조회
	 *
	 * 여러 지급 내역을 조회합니다.
	 *
	 * @throws {@link GetPlatformPayoutsError}
	 */
	getPlatformPayouts: (
		options?: {
			isForTest?: boolean,
			page?: PageInput,
			filter?: PlatformPayoutFilterInput,
		}
	) => Promise<GetPlatformPayoutsResponse>
}
export class GetPlatformPayoutsError extends PayoutError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformPayoutsError.prototype)
		this.name = "GetPlatformPayoutsError"
	}
}

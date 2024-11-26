import { BulkPayoutError } from "./BulkPayoutError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetPlatformBulkPayoutsResponse } from "../../../generated/platform/bulkPayout/GetPlatformBulkPayoutsResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformBulkPayoutFilterInput } from "../../../generated/platform/bulkPayout/PlatformBulkPayoutFilterInput"
import type { PlatformNotEnabledError } from "../../../generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
export function BulkPayoutClient(init: PortOneClientInit): BulkPayoutClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatformBulkPayouts: async (
			options?: {
				isForTest?: boolean,
				page?: PageInput,
				filter?: PlatformBulkPayoutFilterInput,
			}
		): Promise<GetPlatformBulkPayoutsResponse> => {
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
				new URL(`/platform/bulk-payouts?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformBulkPayoutsError(await response.json())
			}
			return response.json()
		},
	}
}
export type BulkPayoutClient = {
	/**
	 * 일괄 지급 내역 다건 조회
	 *
	 * 성공 응답으로 조회된 일괄 지급 내역 리스트와 페이지 정보 및 상태 별 개수 정보를 반환합니다.
	 *
	 * @throws {@link GetPlatformBulkPayoutsError}
	 */
	getPlatformBulkPayouts: (
		options?: {
			isForTest?: boolean,
			page?: PageInput,
			filter?: PlatformBulkPayoutFilterInput,
		}
	) => Promise<GetPlatformBulkPayoutsResponse>
}
export class GetPlatformBulkPayoutsError extends BulkPayoutError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformBulkPayoutsError.prototype)
		this.name = "GetPlatformBulkPayoutsError"
	}
}

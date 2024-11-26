import { AccountTransferError } from "./AccountTransferError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetPlatformAccountTransfersResponse } from "../../../generated/platform/accountTransfer/GetPlatformAccountTransfersResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformAccountTransferFilter } from "../../../generated/platform/accountTransfer/PlatformAccountTransferFilter"
import type { PlatformNotEnabledError } from "../../../generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
export function AccountTransferClient(init: PortOneClientInit): AccountTransferClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatformAccountTransfers: async (
			options?: {
				isForTest?: boolean,
				page?: PageInput,
				filter?: PlatformAccountTransferFilter,
			}
		): Promise<GetPlatformAccountTransfersResponse> => {
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
				new URL(`/platform/account-transfers?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformAccountTransfersError(await response.json())
			}
			return response.json()
		},
	}
}
export type AccountTransferClient = {
	/**
	 * 이체 내역 다건 조회
	 *
	 * 여러 이체 내역을 조회합니다.
	 *
	 * @throws {@link GetPlatformAccountTransfersError}
	 */
	getPlatformAccountTransfers: (
		options?: {
			isForTest?: boolean,
			page?: PageInput,
			filter?: PlatformAccountTransferFilter,
		}
	) => Promise<GetPlatformAccountTransfersResponse>
}
export class GetPlatformAccountTransfersError extends AccountTransferError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformAccountTransfersError.prototype)
		this.name = "GetPlatformAccountTransfersError"
	}
}

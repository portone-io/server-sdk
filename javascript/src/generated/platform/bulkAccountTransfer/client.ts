import { BulkAccountTransferError } from "./BulkAccountTransferError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetPlatformBulkAccountTransfersResponse } from "../../../generated/platform/bulkAccountTransfer/GetPlatformBulkAccountTransfersResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformBulkAccountTransferFilterInput } from "../../../generated/platform/bulkAccountTransfer/PlatformBulkAccountTransferFilterInput"
import type { PlatformNotEnabledError } from "../../../generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function BulkAccountTransferClient(init: PortOneClientInit): BulkAccountTransferClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatformBulkAccountTransfers: async (
			options?: {
				test?: boolean,
				isForTest?: boolean,
				page?: PageInput,
				filter?: PlatformBulkAccountTransferFilterInput,
			}
		): Promise<GetPlatformBulkAccountTransfersResponse> => {
			const test = options?.test
			const isForTest = options?.isForTest
			const page = options?.page
			const filter = options?.filter
			const requestBody = JSON.stringify({
				isForTest,
				page,
				filter,
			})
			const query = [
				["test", test],
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/bulk-account-transfers?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformBulkAccountTransfersError(await response.json())
			}
			return response.json()
		},
	}
}
export type BulkAccountTransferClient = {
	/**
	 * 일괄 이체 내역 다건 조회
	 *
	 * 성공 응답으로 조회된 일괄 이체 내역 리스트와 페이지 정보 및 상태 별 개수 정보를 반환합니다.
	 *
	 * @throws {@link GetPlatformBulkAccountTransfersError}
	 */
	getPlatformBulkAccountTransfers: (
		options?: {
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/**
			 * Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
			 * Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			isForTest?: boolean,
			page?: PageInput,
			filter?: PlatformBulkAccountTransferFilterInput,
		}
	) => Promise<GetPlatformBulkAccountTransfersResponse>
}
export class GetPlatformBulkAccountTransfersError extends BulkAccountTransferError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformBulkAccountTransfersError.prototype)
		this.name = "GetPlatformBulkAccountTransfersError"
	}
}

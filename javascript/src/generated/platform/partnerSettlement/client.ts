import { PartnerSettlementError } from "./PartnerSettlementError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetPlatformPartnerSettlementsResponse } from "../../../generated/platform/partnerSettlement/GetPlatformPartnerSettlementsResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformNotEnabledError } from "../../../generated/platform/PlatformNotEnabledError"
import type { PlatformPartnerSettlementFilterInput } from "../../../generated/platform/partnerSettlement/PlatformPartnerSettlementFilterInput"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function PartnerSettlementClient(init: PortOneClientInit): PartnerSettlementClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatformPartnerSettlements: async (
			options: {
				test?: boolean,
				page?: PageInput,
				filter: PlatformPartnerSettlementFilterInput,
				isForTest?: boolean,
			}
		): Promise<GetPlatformPartnerSettlementsResponse> => {
			const {
				test,
				page,
				filter,
				isForTest,
			} = options
			const requestBody = JSON.stringify({
				page,
				filter,
				isForTest,
			})
			const query = [
				["test", test],
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/partner-settlements?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformPartnerSettlementsError(await response.json())
			}
			return response.json()
		},
	}
}
export type PartnerSettlementClient = {
	/**
	 * 정산 내역 다건 조회
	 *
	 * 여러 정산 내역을 조회합니다.
	 *
	 * @throws {@link GetPlatformPartnerSettlementsError}
	 */
	getPlatformPartnerSettlements: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/** 요청할 페이지 정보 */
			page?: PageInput,
			/** 조회할 정산내역 조건 필터 */
			filter: PlatformPartnerSettlementFilterInput,
			/**
			 * 테스트 모드 여부
			 *
			 * Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
			 * Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			isForTest?: boolean,
		}
	) => Promise<GetPlatformPartnerSettlementsResponse>
}
export class GetPlatformPartnerSettlementsError extends PartnerSettlementError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformPartnerSettlementsError.prototype)
		this.name = "GetPlatformPartnerSettlementsError"
	}
}

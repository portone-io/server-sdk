import { PayoutError } from "./PayoutError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { CompletePlatformPayoutByPartnerSettlementIdsResponse } from "../../../generated/platform/payout/CompletePlatformPayoutByPartnerSettlementIdsResponse"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetPlatformPayoutsResponse } from "../../../generated/platform/payout/GetPlatformPayoutsResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformBulkPayoutIdAlreadyExistsError } from "../../../generated/platform/payout/PlatformBulkPayoutIdAlreadyExistsError"
import type { PlatformDuplicatedPartnerSettlementIdsError } from "../../../generated/platform/payout/PlatformDuplicatedPartnerSettlementIdsError"
import type { PlatformNegativePayoutAmountPartnersError } from "../../../generated/platform/payout/PlatformNegativePayoutAmountPartnersError"
import type { PlatformNoSelectedPartnerSettlementsError } from "../../../generated/platform/payout/PlatformNoSelectedPartnerSettlementsError"
import type { PlatformNonPayablePartnerSettlementsError } from "../../../generated/platform/payout/PlatformNonPayablePartnerSettlementsError"
import type { PlatformNotEnabledError } from "../../../generated/platform/PlatformNotEnabledError"
import type { PlatformPartnerSettlementsNotFoundError } from "../../../generated/platform/PlatformPartnerSettlementsNotFoundError"
import type { PlatformPayoutFilterInput } from "../../../generated/platform/payout/PlatformPayoutFilterInput"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function PayoutClient(init: PortOneClientInit): PayoutClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		completePlatformPayoutByPartnerSettlementIds: async (
			options: {
				test?: boolean,
				bulkPayoutId: string,
				name?: string,
				partnerSettlementIds: string[],
				completedAt?: string,
				isForTest?: boolean,
			}
		): Promise<CompletePlatformPayoutByPartnerSettlementIdsResponse> => {
			const {
				test,
				bulkPayoutId,
				name,
				partnerSettlementIds,
				completedAt,
				isForTest,
			} = options
			const requestBody = JSON.stringify({
				bulkPayoutId,
				name,
				partnerSettlementIds,
				completedAt,
				isForTest,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/partner-settlements/complete-payout?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new CompletePlatformPayoutByPartnerSettlementIdsError(await response.json())
			}
			return response.json()
		},
		getPlatformPayouts: async (
			options?: {
				test?: boolean,
				isForTest?: boolean,
				page?: PageInput,
				filter?: PlatformPayoutFilterInput,
			}
		): Promise<GetPlatformPayoutsResponse> => {
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
	 * 일괄 지급 완료 처리
	 *
	 * 선택한 정산내역 아이디들로 일괄 지급을 완료 처리 합니다.
	 *
	 * @throws {@link CompletePlatformPayoutByPartnerSettlementIdsError}
	 *
	 * @unstable 실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.
	 */
	completePlatformPayoutByPartnerSettlementIds: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			bulkPayoutId: string,
			name?: string,
			partnerSettlementIds: string[],
			/**
			 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
			 * (yyyy-MM-dd)
			 */
			completedAt?: string,
			/**
			 * Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
			 * Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			isForTest?: boolean,
		}
	) => Promise<CompletePlatformPayoutByPartnerSettlementIdsResponse>
	/**
	 * 지급 내역 다건 조회
	 *
	 * 여러 지급 내역을 조회합니다.
	 *
	 * @throws {@link GetPlatformPayoutsError}
	 */
	getPlatformPayouts: (
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
			filter?: PlatformPayoutFilterInput,
		}
	) => Promise<GetPlatformPayoutsResponse>
}
export class CompletePlatformPayoutByPartnerSettlementIdsError extends PayoutError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformBulkPayoutIdAlreadyExistsError | PlatformNegativePayoutAmountPartnersError | PlatformDuplicatedPartnerSettlementIdsError | PlatformNonPayablePartnerSettlementsError | PlatformNotEnabledError | PlatformNoSelectedPartnerSettlementsError | PlatformPartnerSettlementsNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformBulkPayoutIdAlreadyExistsError | PlatformNegativePayoutAmountPartnersError | PlatformDuplicatedPartnerSettlementIdsError | PlatformNonPayablePartnerSettlementsError | PlatformNotEnabledError | PlatformNoSelectedPartnerSettlementsError | PlatformPartnerSettlementsNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CompletePlatformPayoutByPartnerSettlementIdsError.prototype)
		this.name = "CompletePlatformPayoutByPartnerSettlementIdsError"
	}
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

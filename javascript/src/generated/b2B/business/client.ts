import { BusinessError } from "./BusinessError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { B2bExternalServiceError } from "../../../generated/b2B/business/B2bExternalServiceError"
import type { B2bNotEnabledError } from "../../../generated/b2B/business/B2bNotEnabledError"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetB2bBusinessInfosResponse } from "../../../generated/b2B/business/GetB2bBusinessInfosResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function BusinessClient(init: PortOneClientInit): BusinessClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getB2bBusinessInfos: async (
			options: {
				brnList: string[],
			}
		): Promise<GetB2bBusinessInfosResponse> => {
			const {
				brnList,
			} = options
			const requestBody = JSON.stringify({
				brnList,
			})
			const response = await fetch(
				new URL("/b2b/companies/business-info", baseUrl),
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
				throw new GetB2bBusinessInfosError(await response.json())
			}
			return response.json()
		},
	}
}
export type BusinessClient = {
	/**
	 * 사업자 정보 조회
	 *
	 * 요청된 사업자번호에 해당하는 사업자의 정보를 조회합니다.
	 *
	 * @throws {@link GetB2bBusinessInfosError}
	 */
	getB2bBusinessInfos: (
		options: {
			/** 조회할 사업자등록번호 리스트 */
			brnList: string[],
		}
	) => Promise<GetB2bBusinessInfosResponse>
}
export class GetB2bBusinessInfosError extends BusinessError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bBusinessInfosError.prototype)
		this.name = "GetB2bBusinessInfosError"
	}
}

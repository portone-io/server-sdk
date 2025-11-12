import { CompanyError } from "./CompanyError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { B2bExternalServiceError } from "../../../generated/common/B2bExternalServiceError"
import type { B2bNotEnabledError } from "../../../generated/common/B2bNotEnabledError"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetB2bBusinessInfosResponse } from "../../../generated/platform/company/GetB2bBusinessInfosResponse"
import type { GetPlatformCompanyStatePayload } from "../../../generated/platform/company/GetPlatformCompanyStatePayload"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PlatformCompanyNotFoundError } from "../../../generated/platform/company/PlatformCompanyNotFoundError"
import type { PlatformExternalApiFailedError } from "../../../generated/platform/PlatformExternalApiFailedError"
import type { PlatformNotEnabledError } from "../../../generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function CompanyClient(init: PortOneClientInit): CompanyClient {
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
		getPlatformCompanyState: async (
			options: {
				businessRegistrationNumber: string,
				test?: boolean,
			}
		): Promise<GetPlatformCompanyStatePayload> => {
			const {
				businessRegistrationNumber,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/companies/${encodeURIComponent(businessRegistrationNumber)}/state?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformCompanyStateError(await response.json())
			}
			return response.json()
		},
	}
}
export type CompanyClient = {
	/**
	 * 사업자등록 정보조회
	 *
	 * 요청된 사업자등록번호 리스트에 해당하는 사업자등록 정보를 조회합니다.
	 * 해당 API 사용을 위해서는 별도 문의가 필요합니다.
	 *
	 * @throws {@link GetB2bBusinessInfosError}
	 */
	getB2bBusinessInfos: (
		options: {
			/** 조회할 사업자등록번호 리스트 */
			brnList: string[],
		}
	) => Promise<GetB2bBusinessInfosResponse>
	/**
	 * 사업자 조회
	 *
	 * 사업자 정보를 조회합니다. 포트원 서비스에 연동 및 등록되지 않은 사업자도 조회 가능합니다.
	 *
	 * @throws {@link GetPlatformCompanyStateError}
	 */
	getPlatformCompanyState: (
		options: {
			/** 사업자등록번호 */
			businessRegistrationNumber: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
		}
	) => Promise<GetPlatformCompanyStatePayload>
}
export class GetB2bBusinessInfosError extends CompanyError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bBusinessInfosError.prototype)
		this.name = "GetB2bBusinessInfosError"
	}
}
export class GetPlatformCompanyStateError extends CompanyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformCompanyNotFoundError | PlatformExternalApiFailedError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformCompanyNotFoundError | PlatformExternalApiFailedError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformCompanyStateError.prototype)
		this.name = "GetPlatformCompanyStateError"
	}
}

import { CompanyError } from "./CompanyError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
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
		getPlatformCompanyState: async (
			options: {
				businessRegistrationNumber: string,
			}
		): Promise<GetPlatformCompanyStatePayload> => {
			const {
				businessRegistrationNumber,
			} = options
			const response = await fetch(
				new URL(`/platform/companies/${encodeURIComponent(businessRegistrationNumber)}/state`, baseUrl),
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
		}
	) => Promise<GetPlatformCompanyStatePayload>
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

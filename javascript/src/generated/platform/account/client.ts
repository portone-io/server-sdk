import { AccountError } from "./AccountError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { Bank } from "../../../generated/common/Bank"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PlatformAccountHolder } from "../../../generated/platform/account/PlatformAccountHolder"
import type { PlatformExternalApiFailedError } from "../../../generated/platform/PlatformExternalApiFailedError"
import type { PlatformExternalApiTemporarilyFailedError } from "../../../generated/platform/account/PlatformExternalApiTemporarilyFailedError"
import type { PlatformNotEnabledError } from "../../../generated/platform/PlatformNotEnabledError"
import type { PlatformNotSupportedBankError } from "../../../generated/platform/account/PlatformNotSupportedBankError"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function AccountClient(init: PortOneClientInit): AccountClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatformAccountHolder: async (
			options: {
				bank: Bank,
				accountNumber: string,
				birthdate?: string,
				businessRegistrationNumber?: string,
			}
		): Promise<PlatformAccountHolder> => {
			const {
				bank,
				accountNumber,
				birthdate,
				businessRegistrationNumber,
			} = options
			const query = [
				["birthdate", birthdate],
				["businessRegistrationNumber", businessRegistrationNumber],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/bank-accounts/${encodeURIComponent(bank)}/${encodeURIComponent(accountNumber)}/holder?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformAccountHolderError(await response.json())
			}
			return response.json()
		},
	}
}
export type AccountClient = {
	/**
	 * 예금주 조회
	 *
	 * 계좌의 예금주를 조회합니다.
	 *
	 * @throws {@link GetPlatformAccountHolderError}
	 */
	getPlatformAccountHolder: (
		options: {
			/** 은행 */
			bank: Bank,
			/** '-'를 제외한 계좌 번호 */
			accountNumber: string,
			/**
			 * 생년월일
			 *
			 * 실명 조회를 위해 추가로 보낼 수 있습니다. birthdate과 businessRegistrationNumber 중 하나만 사용해야 합니다.
			 */
			birthdate?: string,
			/**
			 * 사업자등록번호
			 *
			 * 실명 조회를 위해 추가로 보낼 수 있습니다. birthdate과 businessRegistrationNumber 중 하나만 사용해야 합니다.
			 */
			businessRegistrationNumber?: string,
		}
	) => Promise<PlatformAccountHolder>
}
export class GetPlatformAccountHolderError extends AccountError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformExternalApiFailedError | PlatformExternalApiTemporarilyFailedError | PlatformNotEnabledError | PlatformNotSupportedBankError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformExternalApiFailedError | PlatformExternalApiTemporarilyFailedError | PlatformNotEnabledError | PlatformNotSupportedBankError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformAccountHolderError.prototype)
		this.name = "GetPlatformAccountHolderError"
	}
}

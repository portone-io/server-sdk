import * as Errors from "../../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { Bank } from "../../../generated/common/Bank"
import type { PlatformAccountHolder } from "../../../generated/platform/account/PlatformAccountHolder"
import type { GetPlatformAccountHolderError as _InternalGetPlatformAccountHolderError } from "../../../generated/platform/account/GetPlatformAccountHolderError"
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
				const errorResponse: _InternalGetPlatformAccountHolderError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_EXTERNAL_API_FAILED":
					throw new Errors.PlatformExternalApiFailedError(errorResponse)
				case "PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED":
					throw new Errors.PlatformExternalApiTemporarilyFailedError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_NOT_SUPPORTED_BANK":
					throw new Errors.PlatformNotSupportedBankError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
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
export type GetPlatformAccountHolderError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformExternalApiFailedError
	| Errors.PlatformExternalApiTemporarilyFailedError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformNotSupportedBankError
	| Errors.UnauthorizedError
export function isGetPlatformAccountHolderError(error: Error): error is GetPlatformAccountHolderError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformExternalApiFailedError
		|| error instanceof Errors.PlatformExternalApiTemporarilyFailedError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformNotSupportedBankError
		|| error instanceof Errors.UnauthorizedError
	)
}

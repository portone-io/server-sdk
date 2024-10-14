import type { Bank } from "../..//common/Bank"
import type { GetPlatformAccountHolderError } from "../..//platform/account/GetPlatformAccountHolderError"
import type { PlatformAccountHolder } from "../..//platform/account/PlatformAccountHolder"
import * as Errors from "../..//errors"
export type { PlatformAccountHolder } from "./PlatformAccountHolder"
/** @ignore */
export function AccountClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): AccountClient {
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
				new URL(`/platform/bank-accounts/${bank}/${accountNumber}/holder?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformAccountHolderError = await response.json()
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
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformExternalApiFailedError} 외부 api 오류
	 * @throws {@link Errors.PlatformExternalApiTemporarilyFailedError} 외부 api의 일시적인 오류
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformNotSupportedBankError} 지원하지 않는 은행인 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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


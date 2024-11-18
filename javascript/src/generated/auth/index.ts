import type { LoginViaApiSecretError } from "..//auth/LoginViaApiSecretError"
import type { LoginViaApiSecretResponse } from "..//auth/LoginViaApiSecretResponse"
import type { RefreshTokenError } from "..//auth/RefreshTokenError"
import type { RefreshTokenResponse } from "..//auth/RefreshTokenResponse"
import * as Errors from "..//errors"
export type { LoginViaApiSecretBody } from "./LoginViaApiSecretBody"
export type { LoginViaApiSecretResponse } from "./LoginViaApiSecretResponse"
export type { RefreshTokenBody } from "./RefreshTokenBody"
export type { RefreshTokenResponse } from "./RefreshTokenResponse"
/** @ignore */
export function AuthClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): AuthClient {
	return {
		loginViaApiSecret: async (
			options: {
				apiSecret: string,
			}
		): Promise<LoginViaApiSecretResponse> => {
			const {
				apiSecret,
			} = options
			const requestBody = JSON.stringify({
				apiSecret,
			})
			const response = await fetch(
				new URL("/login/api-secret", baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: LoginViaApiSecretError = await response.json()
				switch (errorResponse.type) {
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		refreshToken: async (
			options: {
				refreshToken: string,
			}
		): Promise<RefreshTokenResponse> => {
			const {
				refreshToken,
			} = options
			const requestBody = JSON.stringify({
				refreshToken,
			})
			const response = await fetch(
				new URL("/token/refresh", baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: RefreshTokenError = await response.json()
				switch (errorResponse.type) {
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
	}
}
export type AuthClient = {
	/**
	 * API secret 를 사용한 토큰 발급
	 *
	 * API secret 를 통해 API 인증에 사용할 토큰을 가져옵니다.
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	loginViaApiSecret: (
		options: {
			/** 발급받은 API secret */
			apiSecret: string,
		}
	) => Promise<LoginViaApiSecretResponse>
	/**
	 * 토큰 갱신
	 *
	 * 리프레시 토큰을 사용해 유효기간이 연장된 새로운 토큰을 재발급합니다.
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	refreshToken: (
		options: {
			/** 리프레시 토큰 */
			refreshToken: string,
		}
	) => Promise<RefreshTokenResponse>
}


import * as Errors from "../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../client"
import type { LoginViaApiSecretResponse } from "../../generated/auth/LoginViaApiSecretResponse"
import type { RefreshTokenResponse } from "../../generated/auth/RefreshTokenResponse"
import type { LoginViaApiSecretError as _InternalLoginViaApiSecretError } from "../../generated/auth/LoginViaApiSecretError"
import type { RefreshTokenError as _InternalRefreshTokenError } from "../../generated/auth/RefreshTokenError"
export function AuthClient(init: PortOneClientInit): AuthClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
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
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalLoginViaApiSecretError = await response.json()
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
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalRefreshTokenError = await response.json()
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
	 * @throws {@link LoginViaApiSecretError}
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
	 * @throws {@link RefreshTokenError}
	 */
	refreshToken: (
		options: {
			/** 리프레시 토큰 */
			refreshToken: string,
		}
	) => Promise<RefreshTokenResponse>
}
export type LoginViaApiSecretError =
	| Errors.InvalidRequestError
	| Errors.UnauthorizedError
export function isLoginViaApiSecretError(error: Error): error is LoginViaApiSecretError {
	return (
		error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type RefreshTokenError =
	| Errors.InvalidRequestError
	| Errors.UnauthorizedError
export function isRefreshTokenError(error: Error): error is RefreshTokenError {
	return (
		error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.UnauthorizedError
	)
}

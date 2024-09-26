export type * from "./LoginViaApiSecretBody"
export type * from "./LoginViaApiSecretError"
export type * from "./LoginViaApiSecretResponse"
export type * from "./RefreshTokenBody"
export type * from "./RefreshTokenError"
export type * from "./RefreshTokenResponse"
import type { LoginViaApiSecretResponse } from "#generated/auth/LoginViaApiSecretResponse"
import type { RefreshTokenResponse } from "#generated/auth/RefreshTokenResponse"

export type Operations = {
	/**
	 * API secret 를 사용한 토큰 발급
	 *
	 * API secret 를 통해 API 인증에 사용할 토큰을 가져옵니다.
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	loginViaApiSecret: (
		/** 발급받은 API secret */
		apiSecret: string,
	) => Promise<LoginViaApiSecretResponse>
	/**
	 * 토큰 갱신
	 *
	 * 리프레시 토큰을 사용해 유효기간이 연장된 새로운 토큰을 재발급합니다.
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	refreshToken: (
		/** 리프레시 토큰 */
		refreshToken: string,
	) => Promise<RefreshTokenResponse>
}

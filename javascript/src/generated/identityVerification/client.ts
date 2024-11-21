import * as Errors from "../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../client"
import type { ConfirmIdentityVerificationResponse } from "../../generated/identityVerification/ConfirmIdentityVerificationResponse"
import type { IdentityVerification } from "../../generated/identityVerification/IdentityVerification"
import type { IdentityVerificationMethod } from "../../generated/identityVerification/IdentityVerificationMethod"
import type { IdentityVerificationOperator } from "../../generated/identityVerification/IdentityVerificationOperator"
import type { ResendIdentityVerificationResponse } from "../../generated/identityVerification/ResendIdentityVerificationResponse"
import type { SendIdentityVerificationBodyCustomer } from "../../generated/identityVerification/SendIdentityVerificationBodyCustomer"
import type { SendIdentityVerificationResponse } from "../../generated/identityVerification/SendIdentityVerificationResponse"
import type { ConfirmIdentityVerificationError as _InternalConfirmIdentityVerificationError } from "../../generated/identityVerification/ConfirmIdentityVerificationError"
import type { GetIdentityVerificationError as _InternalGetIdentityVerificationError } from "../../generated/identityVerification/GetIdentityVerificationError"
import type { ResendIdentityVerificationError as _InternalResendIdentityVerificationError } from "../../generated/identityVerification/ResendIdentityVerificationError"
import type { SendIdentityVerificationError as _InternalSendIdentityVerificationError } from "../../generated/identityVerification/SendIdentityVerificationError"
export function IdentityVerificationClient(init: PortOneClientInit): IdentityVerificationClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getIdentityVerification: async (
			options: {
				identityVerificationId: string,
				storeId?: string,
			}
		): Promise<IdentityVerification> => {
			const {
				identityVerificationId,
				storeId,
			} = options
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/identity-verifications/${encodeURIComponent(identityVerificationId)}?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetIdentityVerificationError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "IDENTITY_VERIFICATION_NOT_FOUND":
					throw new Errors.IdentityVerificationNotFoundError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		sendIdentityVerification: async (
			options: {
				identityVerificationId: string,
				storeId?: string,
				channelKey: string,
				customer: SendIdentityVerificationBodyCustomer,
				customData?: string,
				bypass?: object,
				operator: IdentityVerificationOperator,
				method: IdentityVerificationMethod,
			}
		): Promise<SendIdentityVerificationResponse> => {
			const {
				identityVerificationId,
				storeId,
				channelKey,
				customer,
				customData,
				bypass,
				operator,
				method,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
				channelKey,
				customer,
				customData,
				bypass,
				operator,
				method,
			})
			const response = await fetch(
				new URL(`/identity-verifications/${encodeURIComponent(identityVerificationId)}/send`, baseUrl),
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
				const errorResponse: _InternalSendIdentityVerificationError = await response.json()
				switch (errorResponse.type) {
				case "CHANNEL_NOT_FOUND":
					throw new Errors.ChannelNotFoundError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "IDENTITY_VERIFICATION_ALREADY_SENT":
					throw new Errors.IdentityVerificationAlreadySentError(errorResponse)
				case "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
					throw new Errors.IdentityVerificationAlreadyVerifiedError(errorResponse)
				case "IDENTITY_VERIFICATION_NOT_FOUND":
					throw new Errors.IdentityVerificationNotFoundError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "MAX_TRANSACTION_COUNT_REACHED":
					throw new Errors.MaxTransactionCountReachedError(errorResponse)
				case "PG_PROVIDER":
					throw new Errors.PgProviderError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		confirmIdentityVerification: async (
			options: {
				identityVerificationId: string,
				storeId?: string,
				otp?: string,
			}
		): Promise<ConfirmIdentityVerificationResponse> => {
			const {
				identityVerificationId,
				storeId,
				otp,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
				otp,
			})
			const response = await fetch(
				new URL(`/identity-verifications/${encodeURIComponent(identityVerificationId)}/confirm`, baseUrl),
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
				const errorResponse: _InternalConfirmIdentityVerificationError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
					throw new Errors.IdentityVerificationAlreadyVerifiedError(errorResponse)
				case "IDENTITY_VERIFICATION_NOT_FOUND":
					throw new Errors.IdentityVerificationNotFoundError(errorResponse)
				case "IDENTITY_VERIFICATION_NOT_SENT":
					throw new Errors.IdentityVerificationNotSentError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PG_PROVIDER":
					throw new Errors.PgProviderError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		resendIdentityVerification: async (
			options: {
				identityVerificationId: string,
				storeId?: string,
			}
		): Promise<ResendIdentityVerificationResponse> => {
			const {
				identityVerificationId,
				storeId,
			} = options
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/identity-verifications/${encodeURIComponent(identityVerificationId)}/resend?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalResendIdentityVerificationError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
					throw new Errors.IdentityVerificationAlreadyVerifiedError(errorResponse)
				case "IDENTITY_VERIFICATION_NOT_FOUND":
					throw new Errors.IdentityVerificationNotFoundError(errorResponse)
				case "IDENTITY_VERIFICATION_NOT_SENT":
					throw new Errors.IdentityVerificationNotSentError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PG_PROVIDER":
					throw new Errors.PgProviderError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
	}
}
export type IdentityVerificationClient = {
	/**
	 * 본인인증 단건 조회
	 *
	 * 주어진 아이디에 대응되는 본인인증 내역을 조회합니다.
	 *
	 * @throws {@link GetIdentityVerificationError}
	 */
	getIdentityVerification: (
		options: {
			/** 조회할 본인인증 아이디 */
			identityVerificationId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<IdentityVerification>
	/**
	 * 본인인증 요청 전송
	 *
	 * SMS 또는 APP 방식을 이용하여 본인인증 요청을 전송합니다.
	 *
	 * @throws {@link SendIdentityVerificationError}
	 */
	sendIdentityVerification: (
		options: {
			/** 본인인증 아이디 */
			identityVerificationId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
			 */
			storeId?: string,
			/** 채널 키 */
			channelKey: string,
			/** 고객 정보 */
			customer: SendIdentityVerificationBodyCustomer,
			/** 사용자 지정 데이터 */
			customData?: string,
			/** PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고) */
			bypass?: object,
			/** 통신사 */
			operator: IdentityVerificationOperator,
			/** 본인인증 방식 */
			method: IdentityVerificationMethod,
		}
	) => Promise<SendIdentityVerificationResponse>
	/**
	 * 본인인증 확인
	 *
	 * 요청된 본인인증에 대한 확인을 진행합니다.
	 *
	 * @throws {@link ConfirmIdentityVerificationError}
	 */
	confirmIdentityVerification: (
		options: {
			/** 본인인증 아이디 */
			identityVerificationId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
			 */
			storeId?: string,
			/**
			 * OTP (One-Time Password)
			 *
			 * SMS 방식에서만 사용됩니다.
			 */
			otp?: string,
		}
	) => Promise<ConfirmIdentityVerificationResponse>
	/**
	 * SMS 본인인증 요청 재전송
	 *
	 * SMS 본인인증 요청을 재전송합니다.
	 *
	 * @throws {@link ResendIdentityVerificationError}
	 */
	resendIdentityVerification: (
		options: {
			/** 본인인증 아이디 */
			identityVerificationId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<ResendIdentityVerificationResponse>
}
export type GetIdentityVerificationError =
	| Errors.ForbiddenError
	| Errors.IdentityVerificationNotFoundError
	| Errors.InvalidRequestError
	| Errors.UnauthorizedError
export function isGetIdentityVerificationError(error: Error): error is GetIdentityVerificationError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.IdentityVerificationNotFoundError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type SendIdentityVerificationError =
	| Errors.ChannelNotFoundError
	| Errors.ForbiddenError
	| Errors.IdentityVerificationAlreadySentError
	| Errors.IdentityVerificationAlreadyVerifiedError
	| Errors.IdentityVerificationNotFoundError
	| Errors.InvalidRequestError
	| Errors.MaxTransactionCountReachedError
	| Errors.PgProviderError
	| Errors.UnauthorizedError
export function isSendIdentityVerificationError(error: Error): error is SendIdentityVerificationError {
	return (
		error instanceof Errors.ChannelNotFoundError
		|| error instanceof Errors.ForbiddenError
		|| error instanceof Errors.IdentityVerificationAlreadySentError
		|| error instanceof Errors.IdentityVerificationAlreadyVerifiedError
		|| error instanceof Errors.IdentityVerificationNotFoundError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.MaxTransactionCountReachedError
		|| error instanceof Errors.PgProviderError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type ConfirmIdentityVerificationError =
	| Errors.ForbiddenError
	| Errors.IdentityVerificationAlreadyVerifiedError
	| Errors.IdentityVerificationNotFoundError
	| Errors.IdentityVerificationNotSentError
	| Errors.InvalidRequestError
	| Errors.PgProviderError
	| Errors.UnauthorizedError
export function isConfirmIdentityVerificationError(error: Error): error is ConfirmIdentityVerificationError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.IdentityVerificationAlreadyVerifiedError
		|| error instanceof Errors.IdentityVerificationNotFoundError
		|| error instanceof Errors.IdentityVerificationNotSentError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PgProviderError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type ResendIdentityVerificationError =
	| Errors.ForbiddenError
	| Errors.IdentityVerificationAlreadyVerifiedError
	| Errors.IdentityVerificationNotFoundError
	| Errors.IdentityVerificationNotSentError
	| Errors.InvalidRequestError
	| Errors.PgProviderError
	| Errors.UnauthorizedError
export function isResendIdentityVerificationError(error: Error): error is ResendIdentityVerificationError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.IdentityVerificationAlreadyVerifiedError
		|| error instanceof Errors.IdentityVerificationNotFoundError
		|| error instanceof Errors.IdentityVerificationNotSentError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PgProviderError
		|| error instanceof Errors.UnauthorizedError
	)
}

import type { ConfirmIdentityVerificationError } from "#generated/identityVerification/ConfirmIdentityVerificationError"
import type { ConfirmIdentityVerificationResponse } from "#generated/identityVerification/ConfirmIdentityVerificationResponse"
import type { GetIdentityVerificationError } from "#generated/identityVerification/GetIdentityVerificationError"
import type { IdentityVerification } from "#generated/identityVerification/IdentityVerification"
import type { IdentityVerificationMethod } from "#generated/identityVerification/IdentityVerificationMethod"
import type { IdentityVerificationOperator } from "#generated/identityVerification/IdentityVerificationOperator"
import type { ResendIdentityVerificationError } from "#generated/identityVerification/ResendIdentityVerificationError"
import type { ResendIdentityVerificationResponse } from "#generated/identityVerification/ResendIdentityVerificationResponse"
import type { SendIdentityVerificationBodyCustomer } from "#generated/identityVerification/SendIdentityVerificationBodyCustomer"
import type { SendIdentityVerificationError } from "#generated/identityVerification/SendIdentityVerificationError"
import type { SendIdentityVerificationResponse } from "#generated/identityVerification/SendIdentityVerificationResponse"
import * as Errors from "#generated/errors"
export type { ConfirmIdentityVerificationBody } from "./ConfirmIdentityVerificationBody"
export type { ConfirmIdentityVerificationResponse } from "./ConfirmIdentityVerificationResponse"
export type { FailedIdentityVerification } from "./FailedIdentityVerification"
export type { IdentityVerification } from "./IdentityVerification"
export type { IdentityVerificationFailure } from "./IdentityVerificationFailure"
export type { IdentityVerificationMethod } from "./IdentityVerificationMethod"
export type { IdentityVerificationOperator } from "./IdentityVerificationOperator"
export type { IdentityVerificationRequestedCustomer } from "./IdentityVerificationRequestedCustomer"
export type { IdentityVerificationVerifiedCustomer } from "./IdentityVerificationVerifiedCustomer"
export type { ReadyIdentityVerification } from "./ReadyIdentityVerification"
export type { ResendIdentityVerificationResponse } from "./ResendIdentityVerificationResponse"
export type { SendIdentityVerificationBody } from "./SendIdentityVerificationBody"
export type { SendIdentityVerificationBodyCustomer } from "./SendIdentityVerificationBodyCustomer"
export type { SendIdentityVerificationResponse } from "./SendIdentityVerificationResponse"
export type { VerifiedIdentityVerification } from "./VerifiedIdentityVerification"
/** @ignore */
export function IdentityVerificationClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): IdentityVerificationClient {
	return {
		getIdentityVerification: async (
			identityVerificationId: string,
		): Promise<IdentityVerification> => {
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/identity-verifications/${identityVerificationId}?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetIdentityVerificationError = await response.json()
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
				channelKey,
				customer,
				customData,
				bypass,
				operator,
				method,
			} = options
			const requestBody = JSON.stringify({
				storeId,
				channelKey,
				customer,
				customData,
				bypass,
				operator,
				method,
			})
			const response = await fetch(
				new URL(`/identity-verifications/${identityVerificationId}/send`, baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: SendIdentityVerificationError = await response.json()
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
			identityVerificationId: string,
			otp?: string,
		): Promise<ConfirmIdentityVerificationResponse> => {
			const requestBody = JSON.stringify({
				storeId,
				otp,
			})
			const response = await fetch(
				new URL(`/identity-verifications/${identityVerificationId}/confirm`, baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: ConfirmIdentityVerificationError = await response.json()
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
			identityVerificationId: string,
		): Promise<ResendIdentityVerificationResponse> => {
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/identity-verifications/${identityVerificationId}/resend?${query}`, baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: ResendIdentityVerificationError = await response.json()
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
	 * @param identityVerificationId
	 * 조회할 본인인증 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.IdentityVerificationNotFoundError} 요청된 본인인증 건이 존재하지 않는 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getIdentityVerification: (
		/** 조회할 본인인증 아이디 */
		identityVerificationId: string,
	) => Promise<IdentityVerification>
	/**
	 * 본인인증 요청 전송
	 *
	 * SMS 또는 APP 방식을 이용하여 본인인증 요청을 전송합니다.
	 *
	 * @throws {@link Errors.ChannelNotFoundError} 요청된 채널이 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.IdentityVerificationAlreadySentError} 본인인증 건이 이미 API로 요청된 상태인 경우
	 * @throws {@link Errors.IdentityVerificationAlreadyVerifiedError} 본인인증 건이 이미 인증 완료된 상태인 경우
	 * @throws {@link Errors.IdentityVerificationNotFoundError} 요청된 본인인증 건이 존재하지 않는 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	sendIdentityVerification: (
		options: {
			/** 본인인증 아이디 */
			identityVerificationId: string,
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
	 * @param identityVerificationId
	 * 본인인증 아이디
	 * @param otp
	 * OTP (One-Time Password)
	 *
	 * SMS 방식에서만 사용됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.IdentityVerificationAlreadyVerifiedError} 본인인증 건이 이미 인증 완료된 상태인 경우
	 * @throws {@link Errors.IdentityVerificationNotFoundError} 요청된 본인인증 건이 존재하지 않는 경우
	 * @throws {@link Errors.IdentityVerificationNotSentError} 본인인증 건이 API로 요청된 상태가 아닌 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	confirmIdentityVerification: (
		/** 본인인증 아이디 */
		identityVerificationId: string,
		/**
		 * OTP (One-Time Password)
		 *
		 * SMS 방식에서만 사용됩니다.
		 */
		otp?: string,
	) => Promise<ConfirmIdentityVerificationResponse>
	/**
	 * SMS 본인인증 요청 재전송
	 *
	 * SMS 본인인증 요청을 재전송합니다.
	 *
	 * @param identityVerificationId
	 * 본인인증 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.IdentityVerificationAlreadyVerifiedError} 본인인증 건이 이미 인증 완료된 상태인 경우
	 * @throws {@link Errors.IdentityVerificationNotFoundError} 요청된 본인인증 건이 존재하지 않는 경우
	 * @throws {@link Errors.IdentityVerificationNotSentError} 본인인증 건이 API로 요청된 상태가 아닌 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	resendIdentityVerification: (
		/** 본인인증 아이디 */
		identityVerificationId: string,
	) => Promise<ResendIdentityVerificationResponse>
}


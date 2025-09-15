import { IdentityVerificationError } from "./IdentityVerificationError"
import type { Unrecognized } from "./../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../client"
import type { ChannelNotFoundError } from "../../generated/common/ChannelNotFoundError"
import type { ConfirmIdentityVerificationResponse } from "../../generated/identityVerification/ConfirmIdentityVerificationResponse"
import type { ForbiddenError } from "../../generated/common/ForbiddenError"
import type { GetIdentityVerificationsResponse } from "../../generated/identityVerification/GetIdentityVerificationsResponse"
import type { IdentityVerification } from "../../generated/identityVerification/IdentityVerification"
import type { IdentityVerificationAlreadySentError } from "../../generated/identityVerification/IdentityVerificationAlreadySentError"
import type { IdentityVerificationAlreadyVerifiedError } from "../../generated/identityVerification/IdentityVerificationAlreadyVerifiedError"
import type { IdentityVerificationFilterInput } from "../../generated/identityVerification/IdentityVerificationFilterInput"
import type { IdentityVerificationMethod } from "../../generated/identityVerification/IdentityVerificationMethod"
import type { IdentityVerificationNotFoundError } from "../../generated/identityVerification/IdentityVerificationNotFoundError"
import type { IdentityVerificationNotSentError } from "../../generated/identityVerification/IdentityVerificationNotSentError"
import type { IdentityVerificationOperator } from "../../generated/identityVerification/IdentityVerificationOperator"
import type { IdentityVerificationSortInput } from "../../generated/identityVerification/IdentityVerificationSortInput"
import type { InvalidRequestError } from "../../generated/common/InvalidRequestError"
import type { MaxTransactionCountReachedError } from "../../generated/common/MaxTransactionCountReachedError"
import type { PageInput } from "../../generated/common/PageInput"
import type { PgProviderError } from "../../generated/common/PgProviderError"
import type { ResendIdentityVerificationResponse } from "../../generated/identityVerification/ResendIdentityVerificationResponse"
import type { SendIdentityVerificationBodyCustomer } from "../../generated/identityVerification/SendIdentityVerificationBodyCustomer"
import type { SendIdentityVerificationResponse } from "../../generated/identityVerification/SendIdentityVerificationResponse"
import type { UnauthorizedError } from "../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function IdentityVerificationClient(init: PortOneClientInit): IdentityVerificationClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
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
				throw new ConfirmIdentityVerificationError(await response.json())
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
				throw new ResendIdentityVerificationError(await response.json())
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
				throw new SendIdentityVerificationError(await response.json())
			}
			return response.json()
		},
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
				throw new GetIdentityVerificationError(await response.json())
			}
			return response.json()
		},
		getIdentityVerifications: async (
			options?: {
				page?: PageInput,
				sort?: IdentityVerificationSortInput,
				filter?: IdentityVerificationFilterInput,
			}
		): Promise<GetIdentityVerificationsResponse> => {
			const page = options?.page
			const sort = options?.sort
			const filter = options?.filter
			const requestBody = JSON.stringify({
				page,
				sort,
				filter,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/identity-verifications?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetIdentityVerificationsError(await response.json())
			}
			return response.json()
		},
	}
}
export type IdentityVerificationClient = {
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
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
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
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<ResendIdentityVerificationResponse>
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
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
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
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<IdentityVerification>
	/**
	 * 본인인증 내역 다건 조회
	 *
	 * 주어진 조건에 맞는 본인인증 내역들을 페이지 기반으로 조회합니다.
	 *
	 * @throws {@link GetIdentityVerificationsError}
	 */
	getIdentityVerifications: (
		options?: {
			/**
			 * 요청할 페이지 정보
			 *
			 * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
			 */
			page?: PageInput,
			/**
			 * 정렬 조건
			 *
			 * 미 입력 시 sortBy: REQUESTED_AT, sortOrder: DESC 으로 기본값이 적용됩니다.
			 */
			sort?: IdentityVerificationSortInput,
			/** 조회할 본인인증 내역 조건 필터 */
			filter?: IdentityVerificationFilterInput,
		}
	) => Promise<GetIdentityVerificationsResponse>
}
export class ConfirmIdentityVerificationError extends IdentityVerificationError {
	declare readonly data: ForbiddenError | IdentityVerificationAlreadyVerifiedError | IdentityVerificationNotFoundError | IdentityVerificationNotSentError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | IdentityVerificationAlreadyVerifiedError | IdentityVerificationNotFoundError | IdentityVerificationNotSentError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ConfirmIdentityVerificationError.prototype)
		this.name = "ConfirmIdentityVerificationError"
	}
}
export class ResendIdentityVerificationError extends IdentityVerificationError {
	declare readonly data: ForbiddenError | IdentityVerificationAlreadyVerifiedError | IdentityVerificationNotFoundError | IdentityVerificationNotSentError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | IdentityVerificationAlreadyVerifiedError | IdentityVerificationNotFoundError | IdentityVerificationNotSentError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ResendIdentityVerificationError.prototype)
		this.name = "ResendIdentityVerificationError"
	}
}
export class SendIdentityVerificationError extends IdentityVerificationError {
	declare readonly data: ChannelNotFoundError | ForbiddenError | IdentityVerificationAlreadySentError | IdentityVerificationAlreadyVerifiedError | IdentityVerificationNotFoundError | InvalidRequestError | MaxTransactionCountReachedError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ChannelNotFoundError | ForbiddenError | IdentityVerificationAlreadySentError | IdentityVerificationAlreadyVerifiedError | IdentityVerificationNotFoundError | InvalidRequestError | MaxTransactionCountReachedError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, SendIdentityVerificationError.prototype)
		this.name = "SendIdentityVerificationError"
	}
}
export class GetIdentityVerificationError extends IdentityVerificationError {
	declare readonly data: ForbiddenError | IdentityVerificationNotFoundError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | IdentityVerificationNotFoundError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetIdentityVerificationError.prototype)
		this.name = "GetIdentityVerificationError"
	}
}
export class GetIdentityVerificationsError extends IdentityVerificationError {
	declare readonly data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetIdentityVerificationsError.prototype)
		this.name = "GetIdentityVerificationsError"
	}
}

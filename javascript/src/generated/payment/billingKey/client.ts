import * as Errors from "../../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { BillingKeyFilterInput } from "../../../generated/payment/billingKey/BillingKeyFilterInput"
import type { BillingKeyInfo } from "../../../generated/payment/billingKey/BillingKeyInfo"
import type { BillingKeySortInput } from "../../../generated/payment/billingKey/BillingKeySortInput"
import type { CustomerInput } from "../../../generated/common/CustomerInput"
import type { DeleteBillingKeyResponse } from "../../../generated/payment/billingKey/DeleteBillingKeyResponse"
import type { GetBillingKeyInfosResponse } from "../../../generated/payment/billingKey/GetBillingKeyInfosResponse"
import type { InstantBillingKeyPaymentMethodInput } from "../../../generated/payment/billingKey/InstantBillingKeyPaymentMethodInput"
import type { IssueBillingKeyResponse } from "../../../generated/payment/billingKey/IssueBillingKeyResponse"
import type { PageInput } from "../../../generated/common/PageInput"
import type { DeleteBillingKeyError as _InternalDeleteBillingKeyError } from "../../../generated/payment/billingKey/DeleteBillingKeyError"
import type { GetBillingKeyInfoError as _InternalGetBillingKeyInfoError } from "../../../generated/payment/billingKey/GetBillingKeyInfoError"
import type { GetBillingKeyInfosError as _InternalGetBillingKeyInfosError } from "../../../generated/payment/billingKey/GetBillingKeyInfosError"
import type { IssueBillingKeyError as _InternalIssueBillingKeyError } from "../../../generated/payment/billingKey/IssueBillingKeyError"
export function BillingKeyClient(init: PortOneClientInit): BillingKeyClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getBillingKeyInfo: async (
			options: {
				billingKey: string,
				storeId?: string,
			}
		): Promise<BillingKeyInfo> => {
			const {
				billingKey,
				storeId,
			} = options
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/billing-keys/${encodeURIComponent(billingKey)}?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetBillingKeyInfoError = await response.json()
				switch (errorResponse.type) {
				case "BILLING_KEY_NOT_FOUND":
					throw new Errors.BillingKeyNotFoundError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		deleteBillingKey: async (
			options: {
				billingKey: string,
				storeId?: string,
			}
		): Promise<DeleteBillingKeyResponse> => {
			const {
				billingKey,
				storeId,
			} = options
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/billing-keys/${encodeURIComponent(billingKey)}?${query}`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalDeleteBillingKeyError = await response.json()
				switch (errorResponse.type) {
				case "BILLING_KEY_ALREADY_DELETED":
					throw new Errors.BillingKeyAlreadyDeletedError(errorResponse)
				case "BILLING_KEY_NOT_FOUND":
					throw new Errors.BillingKeyNotFoundError(errorResponse)
				case "BILLING_KEY_NOT_ISSUED":
					throw new Errors.BillingKeyNotIssuedError(errorResponse)
				case "CHANNEL_SPECIFIC":
					throw new Errors.ChannelSpecificError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PAYMENT_SCHEDULE_ALREADY_EXISTS":
					throw new Errors.PaymentScheduleAlreadyExistsError(errorResponse)
				case "PG_PROVIDER":
					throw new Errors.PgProviderError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getBillingKeyInfos: async (
			options?: {
				page?: PageInput,
				sort?: BillingKeySortInput,
				filter?: BillingKeyFilterInput,
			}
		): Promise<GetBillingKeyInfosResponse> => {
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
				new URL(`/billing-keys?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetBillingKeyInfosError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		issueBillingKey: async (
			options: {
				storeId?: string,
				method: InstantBillingKeyPaymentMethodInput,
				channelKey?: string,
				channelGroupId?: string,
				customer?: CustomerInput,
				customData?: string,
				bypass?: object,
				noticeUrls?: string[],
			}
		): Promise<IssueBillingKeyResponse> => {
			const {
				storeId,
				method,
				channelKey,
				channelGroupId,
				customer,
				customData,
				bypass,
				noticeUrls,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
				method,
				channelKey,
				channelGroupId,
				customer,
				customData,
				bypass,
				noticeUrls,
			})
			const response = await fetch(
				new URL("/billing-keys", baseUrl),
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
				const errorResponse: _InternalIssueBillingKeyError = await response.json()
				switch (errorResponse.type) {
				case "CHANNEL_NOT_FOUND":
					throw new Errors.ChannelNotFoundError(errorResponse)
				case "CHANNEL_SPECIFIC":
					throw new Errors.ChannelSpecificError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
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
export type BillingKeyClient = {
	/**
	 * 빌링키 단건 조회
	 *
	 * 주어진 빌링키에 대응되는 빌링키 정보를 조회합니다.
	 *
	 * @throws {@link GetBillingKeyInfoError}
	 */
	getBillingKeyInfo: (
		options: {
			/** 조회할 빌링키 */
			billingKey: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<BillingKeyInfo>
	/**
	 * 빌링키 삭제
	 *
	 * 빌링키를 삭제합니다.
	 *
	 * @throws {@link DeleteBillingKeyError}
	 */
	deleteBillingKey: (
		options: {
			/** 삭제할 빌링키 */
			billingKey: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<DeleteBillingKeyResponse>
	/**
	 * 빌링키 다건 조회
	 *
	 * 주어진 조건에 맞는 빌링키들을 페이지 기반으로 조회합니다.
	 *
	 * @throws {@link GetBillingKeyInfosError}
	 */
	getBillingKeyInfos: (
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
			 * 미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
			 */
			sort?: BillingKeySortInput,
			/**
			 * 조회할 빌링키 조건 필터
			 *
			 * V1 빌링키 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
			 */
			filter?: BillingKeyFilterInput,
		}
	) => Promise<GetBillingKeyInfosResponse>
	/**
	 * 빌링키 발급
	 *
	 * 빌링키 발급을 요청합니다.
	 *
	 * @throws {@link IssueBillingKeyError}
	 */
	issueBillingKey: (
		options: {
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
			 */
			storeId?: string,
			/** 빌링키 결제 수단 정보 */
			method: InstantBillingKeyPaymentMethodInput,
			/**
			 * 채널 키
			 *
			 * 채널 키 또는 채널 그룹 ID 필수
			 */
			channelKey?: string,
			/**
			 * 채널 그룹 ID
			 *
			 * 채널 키 또는 채널 그룹 ID 필수
			 */
			channelGroupId?: string,
			/** 고객 정보 */
			customer?: CustomerInput,
			/** 사용자 지정 데이터 */
			customData?: string,
			/** PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고) */
			bypass?: object,
			/**
			 * 웹훅 주소
			 *
			 * 빌링키 발급 시 요청을 받을 웹훅 주소입니다.
			 * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
			 * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
			 */
			noticeUrls?: string[],
		}
	) => Promise<IssueBillingKeyResponse>
}
export type GetBillingKeyInfoError =
	| Errors.BillingKeyNotFoundError
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.UnauthorizedError
export function isGetBillingKeyInfoError(error: Error): error is GetBillingKeyInfoError {
	return (
		error instanceof Errors.BillingKeyNotFoundError
		|| error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type DeleteBillingKeyError =
	| Errors.BillingKeyAlreadyDeletedError
	| Errors.BillingKeyNotFoundError
	| Errors.BillingKeyNotIssuedError
	| Errors.ChannelSpecificError
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PaymentScheduleAlreadyExistsError
	| Errors.PgProviderError
	| Errors.UnauthorizedError
export function isDeleteBillingKeyError(error: Error): error is DeleteBillingKeyError {
	return (
		error instanceof Errors.BillingKeyAlreadyDeletedError
		|| error instanceof Errors.BillingKeyNotFoundError
		|| error instanceof Errors.BillingKeyNotIssuedError
		|| error instanceof Errors.ChannelSpecificError
		|| error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PaymentScheduleAlreadyExistsError
		|| error instanceof Errors.PgProviderError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetBillingKeyInfosError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.UnauthorizedError
export function isGetBillingKeyInfosError(error: Error): error is GetBillingKeyInfosError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type IssueBillingKeyError =
	| Errors.ChannelNotFoundError
	| Errors.ChannelSpecificError
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PgProviderError
	| Errors.UnauthorizedError
export function isIssueBillingKeyError(error: Error): error is IssueBillingKeyError {
	return (
		error instanceof Errors.ChannelNotFoundError
		|| error instanceof Errors.ChannelSpecificError
		|| error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PgProviderError
		|| error instanceof Errors.UnauthorizedError
	)
}

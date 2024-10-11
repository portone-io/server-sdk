import type { BillingKeyFilterInput } from "#generated/billingKey/BillingKeyFilterInput"
import type { BillingKeyInfo } from "#generated/billingKey/BillingKeyInfo"
import type { BillingKeySortInput } from "#generated/billingKey/BillingKeySortInput"
import type { CustomerInput } from "#generated/common/CustomerInput"
import type { DeleteBillingKeyError } from "#generated/billingKey/DeleteBillingKeyError"
import type { DeleteBillingKeyResponse } from "#generated/billingKey/DeleteBillingKeyResponse"
import type { GetBillingKeyInfoError } from "#generated/billingKey/GetBillingKeyInfoError"
import type { GetBillingKeyInfosError } from "#generated/billingKey/GetBillingKeyInfosError"
import type { GetBillingKeyInfosResponse } from "#generated/billingKey/GetBillingKeyInfosResponse"
import type { InstantBillingKeyPaymentMethodInput } from "#generated/billingKey/InstantBillingKeyPaymentMethodInput"
import type { IssueBillingKeyError } from "#generated/billingKey/IssueBillingKeyError"
import type { IssueBillingKeyResponse } from "#generated/billingKey/IssueBillingKeyResponse"
import type { PageInput } from "#generated/common/PageInput"
import * as Errors from "#generated/errors"
export type { BillingKeyFailure } from "./BillingKeyFailure"
export type { BillingKeyFilterInput } from "./BillingKeyFilterInput"
export type { BillingKeyInfo } from "./BillingKeyInfo"
export type { BillingKeyInfoSummary } from "./BillingKeyInfoSummary"
export type { BillingKeyPaymentMethod } from "./BillingKeyPaymentMethod"
export type { BillingKeyPaymentMethodCard } from "./BillingKeyPaymentMethodCard"
export type { BillingKeyPaymentMethodEasyPay } from "./BillingKeyPaymentMethodEasyPay"
export type { BillingKeyPaymentMethodEasyPayCharge } from "./BillingKeyPaymentMethodEasyPayCharge"
export type { BillingKeyPaymentMethodEasyPayMethod } from "./BillingKeyPaymentMethodEasyPayMethod"
export type { BillingKeyPaymentMethodMobile } from "./BillingKeyPaymentMethodMobile"
export type { BillingKeyPaymentMethodPaypal } from "./BillingKeyPaymentMethodPaypal"
export type { BillingKeyPaymentMethodTransfer } from "./BillingKeyPaymentMethodTransfer"
export type { BillingKeyPaymentMethodType } from "./BillingKeyPaymentMethodType"
export type { BillingKeySortBy } from "./BillingKeySortBy"
export type { BillingKeySortInput } from "./BillingKeySortInput"
export type { BillingKeyStatus } from "./BillingKeyStatus"
export type { BillingKeyTextSearch } from "./BillingKeyTextSearch"
export type { BillingKeyTextSearchField } from "./BillingKeyTextSearchField"
export type { BillingKeyTimeRangeField } from "./BillingKeyTimeRangeField"
export type { ChannelSpecificFailure } from "./ChannelSpecificFailure"
export type { ChannelSpecificFailureInvalidRequest } from "./ChannelSpecificFailureInvalidRequest"
export type { ChannelSpecificFailurePgProvider } from "./ChannelSpecificFailurePgProvider"
export type { DeleteBillingKeyResponse } from "./DeleteBillingKeyResponse"
export type { DeletedBillingKeyInfo } from "./DeletedBillingKeyInfo"
export type { FailedPgBillingKeyIssueResponse } from "./FailedPgBillingKeyIssueResponse"
export type { GetBillingKeyInfosBody } from "./GetBillingKeyInfosBody"
export type { GetBillingKeyInfosResponse } from "./GetBillingKeyInfosResponse"
export type { InstantBillingKeyPaymentMethodInput } from "./InstantBillingKeyPaymentMethodInput"
export type { InstantBillingKeyPaymentMethodInputCard } from "./InstantBillingKeyPaymentMethodInputCard"
export type { IssueBillingKeyBody } from "./IssueBillingKeyBody"
export type { IssueBillingKeyResponse } from "./IssueBillingKeyResponse"
export type { IssuedBillingKeyInfo } from "./IssuedBillingKeyInfo"
export type { IssuedPgBillingKeyIssueResponse } from "./IssuedPgBillingKeyIssueResponse"
export type { PgBillingKeyIssueResponse } from "./PgBillingKeyIssueResponse"
/** @ignore */
export function BillingKeyClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): BillingKeyClient {
	return {
		getBillingKeyInfo: async (
			billingKey: string,
		): Promise<BillingKeyInfo> => {
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/billing-keys/${billingKey}?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetBillingKeyInfoError = await response.json()
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
			billingKey: string,
		): Promise<DeleteBillingKeyResponse> => {
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/billing-keys/${billingKey}?${query}`, baseUrl),
				{
					method: "delete",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: DeleteBillingKeyError = await response.json()
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
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetBillingKeyInfosError = await response.json()
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
				method,
				channelKey,
				channelGroupId,
				customer,
				customData,
				bypass,
				noticeUrls,
			} = options
			const requestBody = JSON.stringify({
				storeId,
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
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: IssueBillingKeyError = await response.json()
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
	 * @param billingKey
	 * 조회할 빌링키
	 *
	 * @throws {@link Errors.BillingKeyNotFoundError} 빌링키가 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getBillingKeyInfo: (
		/** 조회할 빌링키 */
		billingKey: string,
	) => Promise<BillingKeyInfo>
	/**
	 * 빌링키 삭제
	 *
	 * 빌링키를 삭제합니다.
	 *
	 * @param billingKey
	 * 삭제할 빌링키
	 *
	 * @throws {@link Errors.BillingKeyAlreadyDeletedError} 빌링키가 이미 삭제된 경우
	 * @throws {@link Errors.BillingKeyNotFoundError} 빌링키가 존재하지 않는 경우
	 * @throws {@link Errors.BillingKeyNotIssuedError} BillingKeyNotIssuedError
	 * @throws {@link Errors.ChannelSpecificError} 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentScheduleAlreadyExistsError} 결제 예약건이 이미 존재하는 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	deleteBillingKey: (
		/** 삭제할 빌링키 */
		billingKey: string,
	) => Promise<DeleteBillingKeyResponse>
	/**
	 * 빌링키 다건 조회
	 *
	 * 주어진 조건에 맞는 빌링키들을 페이지 기반으로 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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
	 * @throws {@link Errors.ChannelNotFoundError} 요청된 채널이 존재하지 않는 경우
	 * @throws {@link Errors.ChannelSpecificError} 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	issueBillingKey: (
		options: {
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


import { BillingKeyError } from "./BillingKeyError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { BillingKeyAlreadyDeletedError } from "../../../generated/common/BillingKeyAlreadyDeletedError"
import type { BillingKeyFilterInput } from "../../../generated/payment/billingKey/BillingKeyFilterInput"
import type { BillingKeyInfo } from "../../../generated/payment/billingKey/BillingKeyInfo"
import type { BillingKeyNotFoundError } from "../../../generated/common/BillingKeyNotFoundError"
import type { BillingKeyNotIssuedError } from "../../../generated/payment/billingKey/BillingKeyNotIssuedError"
import type { BillingKeySortInput } from "../../../generated/payment/billingKey/BillingKeySortInput"
import type { ChannelNotFoundError } from "../../../generated/common/ChannelNotFoundError"
import type { ChannelSpecificError } from "../../../generated/payment/billingKey/ChannelSpecificError"
import type { CustomerInput } from "../../../generated/common/CustomerInput"
import type { DeleteBillingKeyResponse } from "../../../generated/payment/billingKey/DeleteBillingKeyResponse"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetBillingKeyInfosResponse } from "../../../generated/payment/billingKey/GetBillingKeyInfosResponse"
import type { InstantBillingKeyPaymentMethodInput } from "../../../generated/payment/billingKey/InstantBillingKeyPaymentMethodInput"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { IssueBillingKeyResponse } from "../../../generated/payment/billingKey/IssueBillingKeyResponse"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PaymentScheduleAlreadyExistsError } from "../../../generated/common/PaymentScheduleAlreadyExistsError"
import type { PgProviderError } from "../../../generated/common/PgProviderError"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function BillingKeyClient(init: PortOneClientInit): BillingKeyClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
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
				throw new GetBillingKeyInfosError(await response.json())
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
				throw new IssueBillingKeyError(await response.json())
			}
			return response.json()
		},
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
				throw new GetBillingKeyInfoError(await response.json())
			}
			return response.json()
		},
		deleteBillingKey: async (
			options: {
				billingKey: string,
				storeId?: string,
				reason?: string,
			}
		): Promise<DeleteBillingKeyResponse> => {
			const {
				billingKey,
				storeId,
				reason,
			} = options
			const query = [
				["storeId", storeId],
				["reason", reason],
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
				throw new DeleteBillingKeyError(await response.json())
			}
			return response.json()
		},
	}
}
export type BillingKeyClient = {
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
			/**
			 * 사유
			 *
			 * 네이버페이: 자동결제 해지 사유입니다. 명시가 필요합니다.
			 */
			reason?: string,
		}
	) => Promise<DeleteBillingKeyResponse>
}
export class GetBillingKeyInfosError extends BillingKeyError {
	declare readonly data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetBillingKeyInfosError.prototype)
		this.name = "GetBillingKeyInfosError"
	}
}
export class IssueBillingKeyError extends BillingKeyError {
	declare readonly data: ChannelNotFoundError | ChannelSpecificError | ForbiddenError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ChannelNotFoundError | ChannelSpecificError | ForbiddenError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, IssueBillingKeyError.prototype)
		this.name = "IssueBillingKeyError"
	}
}
export class GetBillingKeyInfoError extends BillingKeyError {
	declare readonly data: BillingKeyNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: BillingKeyNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetBillingKeyInfoError.prototype)
		this.name = "GetBillingKeyInfoError"
	}
}
export class DeleteBillingKeyError extends BillingKeyError {
	declare readonly data: BillingKeyAlreadyDeletedError | BillingKeyNotFoundError | BillingKeyNotIssuedError | ChannelSpecificError | ForbiddenError | InvalidRequestError | PaymentScheduleAlreadyExistsError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: BillingKeyAlreadyDeletedError | BillingKeyNotFoundError | BillingKeyNotIssuedError | ChannelSpecificError | ForbiddenError | InvalidRequestError | PaymentScheduleAlreadyExistsError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, DeleteBillingKeyError.prototype)
		this.name = "DeleteBillingKeyError"
	}
}

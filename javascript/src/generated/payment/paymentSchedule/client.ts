import * as Errors from "../../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { BillingKeyPaymentInput } from "../../../generated/common/BillingKeyPaymentInput"
import type { CreatePaymentScheduleResponse } from "../../../generated/payment/paymentSchedule/CreatePaymentScheduleResponse"
import type { GetPaymentSchedulesResponse } from "../../../generated/payment/paymentSchedule/GetPaymentSchedulesResponse"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PaymentSchedule } from "../../../generated/payment/paymentSchedule/PaymentSchedule"
import type { PaymentScheduleFilterInput } from "../../../generated/payment/paymentSchedule/PaymentScheduleFilterInput"
import type { PaymentScheduleSortInput } from "../../../generated/payment/paymentSchedule/PaymentScheduleSortInput"
import type { RevokePaymentSchedulesResponse } from "../../../generated/payment/paymentSchedule/RevokePaymentSchedulesResponse"
import type { CreatePaymentScheduleError as _InternalCreatePaymentScheduleError } from "../../../generated/payment/paymentSchedule/CreatePaymentScheduleError"
import type { GetPaymentScheduleError as _InternalGetPaymentScheduleError } from "../../../generated/payment/paymentSchedule/GetPaymentScheduleError"
import type { GetPaymentSchedulesError as _InternalGetPaymentSchedulesError } from "../../../generated/payment/paymentSchedule/GetPaymentSchedulesError"
import type { RevokePaymentSchedulesError as _InternalRevokePaymentSchedulesError } from "../../../generated/payment/paymentSchedule/RevokePaymentSchedulesError"
export function PaymentScheduleClient(init: PortOneClientInit): PaymentScheduleClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPaymentSchedule: async (
			options: {
				paymentScheduleId: string,
				storeId?: string,
			}
		): Promise<PaymentSchedule> => {
			const {
				paymentScheduleId,
				storeId,
			} = options
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payment-schedules/${encodeURIComponent(paymentScheduleId)}?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPaymentScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PAYMENT_SCHEDULE_NOT_FOUND":
					throw new Errors.PaymentScheduleNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPaymentSchedules: async (
			options?: {
				page?: PageInput,
				sort?: PaymentScheduleSortInput,
				filter?: PaymentScheduleFilterInput,
			}
		): Promise<GetPaymentSchedulesResponse> => {
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
				new URL(`/payment-schedules?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPaymentSchedulesError = await response.json()
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
		revokePaymentSchedules: async (
			options?: {
				storeId?: string,
				billingKey?: string,
				scheduleIds?: string[],
			}
		): Promise<RevokePaymentSchedulesResponse> => {
			const storeId = options?.storeId
			const billingKey = options?.billingKey
			const scheduleIds = options?.scheduleIds
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
				billingKey,
				scheduleIds,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payment-schedules?${query}`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalRevokePaymentSchedulesError = await response.json()
				switch (errorResponse.type) {
				case "BILLING_KEY_ALREADY_DELETED":
					throw new Errors.BillingKeyAlreadyDeletedError(errorResponse)
				case "BILLING_KEY_NOT_FOUND":
					throw new Errors.BillingKeyNotFoundError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PAYMENT_SCHEDULE_ALREADY_PROCESSED":
					throw new Errors.PaymentScheduleAlreadyProcessedError(errorResponse)
				case "PAYMENT_SCHEDULE_ALREADY_REVOKED":
					throw new Errors.PaymentScheduleAlreadyRevokedError(errorResponse)
				case "PAYMENT_SCHEDULE_NOT_FOUND":
					throw new Errors.PaymentScheduleNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		createPaymentSchedule: async (
			options: {
				paymentId: string,
				payment: BillingKeyPaymentInput,
				timeToPay: string,
			}
		): Promise<CreatePaymentScheduleResponse> => {
			const {
				paymentId,
				payment,
				timeToPay,
			} = options
			const requestBody = JSON.stringify({
				payment,
				timeToPay,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/schedule`, baseUrl),
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
				const errorResponse: _InternalCreatePaymentScheduleError = await response.json()
				switch (errorResponse.type) {
				case "ALREADY_PAID_OR_WAITING":
					throw new Errors.AlreadyPaidOrWaitingError(errorResponse)
				case "BILLING_KEY_ALREADY_DELETED":
					throw new Errors.BillingKeyAlreadyDeletedError(errorResponse)
				case "BILLING_KEY_NOT_FOUND":
					throw new Errors.BillingKeyNotFoundError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PAYMENT_SCHEDULE_ALREADY_EXISTS":
					throw new Errors.PaymentScheduleAlreadyExistsError(errorResponse)
				case "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
					throw new Errors.SumOfPartsExceedsTotalAmountError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
	}
}
export type PaymentScheduleClient = {
	/**
	 * 결제 예약 단건 조회
	 *
	 * 주어진 아이디에 대응되는 결제 예약 건을 조회합니다.
	 *
	 * @throws {@link GetPaymentScheduleError}
	 */
	getPaymentSchedule: (
		options: {
			/** 조회할 결제 예약 건 아이디 */
			paymentScheduleId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<PaymentSchedule>
	/**
	 * 결제 예약 다건 조회
	 *
	 * 주어진 조건에 맞는 결제 예약 건들을 조회합니다.
	 * `filter.from`, `filter.until` 파라미터의 기본값이 결제 시점 기준 지난 90일에 속하는 건을 조회하도록 되어 있으니, 미래 예약 상태의 건을 조회하기 위해서는 해당 파라미터를 직접 설정해 주셔야 합니다.
	 *
	 * @throws {@link GetPaymentSchedulesError}
	 */
	getPaymentSchedules: (
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
			sort?: PaymentScheduleSortInput,
			/** 조회할 결제 예약 건의 조건 필터 */
			filter?: PaymentScheduleFilterInput,
		}
	) => Promise<GetPaymentSchedulesResponse>
	/**
	 * 결제 예약 취소
	 *
	 * 결제 예약 건을 취소합니다.
	 * billingKey, scheduleIds 중 하나 이상은 필수로 입력합니다.
	 * billingKey 만 입력된 경우 -> 해당 빌링키로 예약된 모든 결제 예약 건들이 취소됩니다.
	 * scheduleIds 만 입력된 경우 -> 입력된 결제 예약 건 아이디에 해당하는 예약 건들이 취소됩니다.
	 * billingKey, scheduleIds 모두 입력된 경우 -> 입력된 결제 예약 건 아이디에 해당하는 예약 건들이 취소됩니다. 단, 예약한 빌링키가 입력된 빌링키와 일치하지 않으면 실패합니다.
	 * 위 정책에 따라 선택된 결제 예약 건들 중 하나라도 취소에 실패할 경우, 모든 취소 요청이 실패합니다.
	 *
	 * @throws {@link RevokePaymentSchedulesError}
	 */
	revokePaymentSchedules: (
		options?: {
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
			 */
			storeId?: string,
			/** 빌링키 */
			billingKey?: string,
			/** 결제 예약 건 아이디 목록 */
			scheduleIds?: string[],
		}
	) => Promise<RevokePaymentSchedulesResponse>
	/**
	 * 결제 예약
	 *
	 * 결제를 예약합니다.
	 *
	 * @throws {@link CreatePaymentScheduleError}
	 */
	createPaymentSchedule: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/** 빌링키 결제 입력 정보 */
			payment: BillingKeyPaymentInput,
			/**
			 * 결제 예정 시점
			 * (RFC 3339 date-time)
			 */
			timeToPay: string,
		}
	) => Promise<CreatePaymentScheduleResponse>
}
export type GetPaymentScheduleError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PaymentScheduleNotFoundError
	| Errors.UnauthorizedError
export function isGetPaymentScheduleError(error: Error): error is GetPaymentScheduleError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PaymentScheduleNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPaymentSchedulesError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.UnauthorizedError
export function isGetPaymentSchedulesError(error: Error): error is GetPaymentSchedulesError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type RevokePaymentSchedulesError =
	| Errors.BillingKeyAlreadyDeletedError
	| Errors.BillingKeyNotFoundError
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PaymentScheduleAlreadyProcessedError
	| Errors.PaymentScheduleAlreadyRevokedError
	| Errors.PaymentScheduleNotFoundError
	| Errors.UnauthorizedError
export function isRevokePaymentSchedulesError(error: Error): error is RevokePaymentSchedulesError {
	return (
		error instanceof Errors.BillingKeyAlreadyDeletedError
		|| error instanceof Errors.BillingKeyNotFoundError
		|| error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PaymentScheduleAlreadyProcessedError
		|| error instanceof Errors.PaymentScheduleAlreadyRevokedError
		|| error instanceof Errors.PaymentScheduleNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CreatePaymentScheduleError =
	| Errors.AlreadyPaidOrWaitingError
	| Errors.BillingKeyAlreadyDeletedError
	| Errors.BillingKeyNotFoundError
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PaymentScheduleAlreadyExistsError
	| Errors.SumOfPartsExceedsTotalAmountError
	| Errors.UnauthorizedError
export function isCreatePaymentScheduleError(error: Error): error is CreatePaymentScheduleError {
	return (
		error instanceof Errors.AlreadyPaidOrWaitingError
		|| error instanceof Errors.BillingKeyAlreadyDeletedError
		|| error instanceof Errors.BillingKeyNotFoundError
		|| error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PaymentScheduleAlreadyExistsError
		|| error instanceof Errors.SumOfPartsExceedsTotalAmountError
		|| error instanceof Errors.UnauthorizedError
	)
}

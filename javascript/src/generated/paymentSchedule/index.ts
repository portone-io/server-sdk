import type { BillingKeyPaymentInput } from "#generated/common/BillingKeyPaymentInput"
import type { CreatePaymentScheduleError } from "#generated/paymentSchedule/CreatePaymentScheduleError"
import type { CreatePaymentScheduleResponse } from "#generated/paymentSchedule/CreatePaymentScheduleResponse"
import type { GetPaymentScheduleError } from "#generated/paymentSchedule/GetPaymentScheduleError"
import type { GetPaymentSchedulesError } from "#generated/paymentSchedule/GetPaymentSchedulesError"
import type { GetPaymentSchedulesResponse } from "#generated/paymentSchedule/GetPaymentSchedulesResponse"
import type { PageInput } from "#generated/common/PageInput"
import type { PaymentSchedule } from "#generated/paymentSchedule/PaymentSchedule"
import type { PaymentScheduleFilterInput } from "#generated/paymentSchedule/PaymentScheduleFilterInput"
import type { PaymentScheduleSortInput } from "#generated/paymentSchedule/PaymentScheduleSortInput"
import type { RevokePaymentSchedulesError } from "#generated/paymentSchedule/RevokePaymentSchedulesError"
import type { RevokePaymentSchedulesResponse } from "#generated/paymentSchedule/RevokePaymentSchedulesResponse"
import * as Errors from "#generated/errors"
export type { CreatePaymentScheduleBody } from "./CreatePaymentScheduleBody"
export type { CreatePaymentScheduleResponse } from "./CreatePaymentScheduleResponse"
export type { FailedPaymentSchedule } from "./FailedPaymentSchedule"
export type { GetPaymentSchedulesBody } from "./GetPaymentSchedulesBody"
export type { GetPaymentSchedulesResponse } from "./GetPaymentSchedulesResponse"
export type { PaymentSchedule } from "./PaymentSchedule"
export type { PaymentScheduleFilterInput } from "./PaymentScheduleFilterInput"
export type { PaymentScheduleSortBy } from "./PaymentScheduleSortBy"
export type { PaymentScheduleSortInput } from "./PaymentScheduleSortInput"
export type { PaymentScheduleStatus } from "./PaymentScheduleStatus"
export type { PaymentScheduleSummary } from "./PaymentScheduleSummary"
export type { PendingPaymentSchedule } from "./PendingPaymentSchedule"
export type { RevokePaymentSchedulesBody } from "./RevokePaymentSchedulesBody"
export type { RevokePaymentSchedulesResponse } from "./RevokePaymentSchedulesResponse"
export type { RevokedPaymentSchedule } from "./RevokedPaymentSchedule"
export type { ScheduledPaymentSchedule } from "./ScheduledPaymentSchedule"
export type { StartedPaymentSchedule } from "./StartedPaymentSchedule"
export type { SucceededPaymentSchedule } from "./SucceededPaymentSchedule"
/** @ignore */
export function PaymentScheduleClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): PaymentScheduleClient {
	return {
		getPaymentSchedule: async (
			paymentScheduleId: string,
		): Promise<PaymentSchedule> => {
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payment-schedules/${paymentScheduleId}?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPaymentScheduleError = await response.json()
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
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPaymentSchedulesError = await response.json()
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
				billingKey?: string,
				scheduleIds?: string[],
			}
		): Promise<RevokePaymentSchedulesResponse> => {
			const billingKey = options?.billingKey
			const scheduleIds = options?.scheduleIds
			const requestBody = JSON.stringify({
				storeId,
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
					method: "delete",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: RevokePaymentSchedulesError = await response.json()
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
			paymentId: string,
			payment: BillingKeyPaymentInput,
			timeToPay: string,
		): Promise<CreatePaymentScheduleResponse> => {
			const requestBody = JSON.stringify({
				payment,
				timeToPay,
			})
			const response = await fetch(
				new URL(`/payments/${paymentId}/schedule`, baseUrl),
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
				const errorResponse: CreatePaymentScheduleError = await response.json()
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
	 * @param paymentScheduleId
	 * 조회할 결제 예약 건 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentScheduleNotFoundError} 결제 예약건이 존재하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPaymentSchedule: (
		/** 조회할 결제 예약 건 아이디 */
		paymentScheduleId: string,
	) => Promise<PaymentSchedule>
	/**
	 * 결제 예약 다건 조회
	 *
	 * 주어진 조건에 맞는 결제 예약 건들을 조회합니다.
	 * `filter.from`, `filter.until` 파라미터의 기본값이 결제 시점 기준 지난 90일에 속하는 건을 조회하도록 되어 있으니, 미래 예약 상태의 건을 조회하기 위해서는 해당 파라미터를 직접 설정해 주셔야 합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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
	 *
	 * @throws {@link Errors.BillingKeyAlreadyDeletedError} 빌링키가 이미 삭제된 경우
	 * @throws {@link Errors.BillingKeyNotFoundError} 빌링키가 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentScheduleAlreadyProcessedError} 결제 예약건이 이미 처리된 경우
	 * @throws {@link Errors.PaymentScheduleAlreadyRevokedError} 결제 예약건이 이미 취소된 경우
	 * @throws {@link Errors.PaymentScheduleNotFoundError} 결제 예약건이 존재하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	revokePaymentSchedules: (
		options?: {
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
	 * @param paymentId
	 * 결제 건 아이디
	 * @param payment
	 * 빌링키 결제 입력 정보
	 * @param timeToPay
	 * 결제 예정 시점
	 *
	 * @throws {@link Errors.AlreadyPaidOrWaitingError} 결제가 이미 완료되었거나 대기중인 경우
	 * @throws {@link Errors.BillingKeyAlreadyDeletedError} 빌링키가 이미 삭제된 경우
	 * @throws {@link Errors.BillingKeyNotFoundError} 빌링키가 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentScheduleAlreadyExistsError} 결제 예약건이 이미 존재하는 경우
	 * @throws {@link Errors.SumOfPartsExceedsTotalAmountError} 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	createPaymentSchedule: (
		/** 결제 건 아이디 */
		paymentId: string,
		/** 빌링키 결제 입력 정보 */
		payment: BillingKeyPaymentInput,
		/**
		 * 결제 예정 시점
		 * (RFC 3339 date-time)
		 */
		timeToPay: string,
	) => Promise<CreatePaymentScheduleResponse>
}


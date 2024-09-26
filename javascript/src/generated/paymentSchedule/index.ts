export type * from "./AlreadyPaidOrWaitingError"
export type * from "./CreatePaymentScheduleBody"
export type * from "./CreatePaymentScheduleError"
export type * from "./CreatePaymentScheduleResponse"
export type * from "./FailedPaymentSchedule"
export type * from "./GetPaymentScheduleError"
export type * from "./GetPaymentSchedulesBody"
export type * from "./GetPaymentSchedulesError"
export type * from "./GetPaymentSchedulesResponse"
export type * from "./PaymentSchedule"
export type * from "./PaymentScheduleAlreadyProcessedError"
export type * from "./PaymentScheduleAlreadyRevokedError"
export type * from "./PaymentScheduleFilterInput"
export type * from "./PaymentScheduleNotFoundError"
export type * from "./PaymentScheduleSortBy"
export type * from "./PaymentScheduleSortInput"
export type * from "./PaymentScheduleStatus"
export type * from "./PaymentScheduleSummary"
export type * from "./PendingPaymentSchedule"
export type * from "./RevokePaymentSchedulesBody"
export type * from "./RevokePaymentSchedulesError"
export type * from "./RevokePaymentSchedulesResponse"
export type * from "./RevokedPaymentSchedule"
export type * from "./ScheduledPaymentSchedule"
export type * from "./StartedPaymentSchedule"
export type * from "./SucceededPaymentSchedule"
import type { BillingKeyPaymentInput } from "#generated/common/BillingKeyPaymentInput"
import type { CreatePaymentScheduleResponse } from "#generated/paymentSchedule/CreatePaymentScheduleResponse"
import type { GetPaymentSchedulesResponse } from "#generated/paymentSchedule/GetPaymentSchedulesResponse"
import type { PageInput } from "#generated/common/PageInput"
import type { PaymentSchedule } from "#generated/paymentSchedule/PaymentSchedule"
import type { PaymentScheduleFilterInput } from "#generated/paymentSchedule/PaymentScheduleFilterInput"
import type { PaymentScheduleSortInput } from "#generated/paymentSchedule/PaymentScheduleSortInput"
import type { RevokePaymentSchedulesResponse } from "#generated/paymentSchedule/RevokePaymentSchedulesResponse"

export type Operations = {
	/**
	 * 결제 예약 단건 조회
	 *
	 * 주어진 아이디에 대응되는 결제 예약 건을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentScheduleNotFoundError} 결제 예약건이 존재하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
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
	 * @throws {@link Errors.AlreadyPaidOrWaitingError} 결제가 이미 완료되었거나 대기중인 경우
	 * @throws {@link Errors.BillingKeyAlreadyDeletedError} 빌링키가 이미 삭제된 경우
	 * @throws {@link Errors.BillingKeyNotFoundError} 빌링키가 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentScheduleAlreadyExistsError} 결제 예약건이 이미 존재하는 경우
	 * @throws {@link Errors.SumOfPartsExceedsTotalAmountError} 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
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

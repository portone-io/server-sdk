import type { Unrecognized } from "./../../../utils/unrecognized"
import type { AlreadyPaidOrWaitingError } from "./../../payment/paymentSchedule/AlreadyPaidOrWaitingError"
import type { BillingKeyAlreadyDeletedError } from "./../../common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError } from "./../../common/BillingKeyNotFoundError"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PaymentScheduleAlreadyExistsError } from "./../../common/PaymentScheduleAlreadyExistsError"
import type { SumOfPartsExceedsTotalAmountError } from "./../../common/SumOfPartsExceedsTotalAmountError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type CreatePaymentScheduleError =
	| AlreadyPaidOrWaitingError
	| BillingKeyAlreadyDeletedError
	| BillingKeyNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| PaymentScheduleAlreadyExistsError
	| SumOfPartsExceedsTotalAmountError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedCreatePaymentScheduleError(entity: CreatePaymentScheduleError): entity is { readonly type: Unrecognized } {
	return entity.type !== "ALREADY_PAID_OR_WAITING"
		&& entity.type !== "BILLING_KEY_ALREADY_DELETED"
		&& entity.type !== "BILLING_KEY_NOT_FOUND"
		&& entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PAYMENT_SCHEDULE_ALREADY_EXISTS"
		&& entity.type !== "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT"
		&& entity.type !== "UNAUTHORIZED"
}

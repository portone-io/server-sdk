import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PaymentScheduleNotFoundError } from "#generated/payment/paymentSchedule/PaymentScheduleNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetPaymentScheduleError =
	| ForbiddenError
	| InvalidRequestError
	| PaymentScheduleNotFoundError
	| UnauthorizedError

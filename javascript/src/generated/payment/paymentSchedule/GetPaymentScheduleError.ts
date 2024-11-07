import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PaymentScheduleNotFoundError } from "./../../payment/paymentSchedule/PaymentScheduleNotFoundError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type GetPaymentScheduleError =
	| ForbiddenError
	| InvalidRequestError
	| PaymentScheduleNotFoundError
	| UnauthorizedError

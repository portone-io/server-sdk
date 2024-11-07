import type { BillingKeyAlreadyDeletedError } from "./../../common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError } from "./../../common/BillingKeyNotFoundError"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PaymentScheduleAlreadyProcessedError } from "./../../payment/paymentSchedule/PaymentScheduleAlreadyProcessedError"
import type { PaymentScheduleAlreadyRevokedError } from "./../../payment/paymentSchedule/PaymentScheduleAlreadyRevokedError"
import type { PaymentScheduleNotFoundError } from "./../../payment/paymentSchedule/PaymentScheduleNotFoundError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type RevokePaymentSchedulesError =
	| BillingKeyAlreadyDeletedError
	| BillingKeyNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| PaymentScheduleAlreadyProcessedError
	| PaymentScheduleAlreadyRevokedError
	| PaymentScheduleNotFoundError
	| UnauthorizedError

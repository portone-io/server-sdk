import type { BillingKeyAlreadyDeletedError } from "#generated/common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError } from "#generated/common/BillingKeyNotFoundError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PaymentScheduleAlreadyProcessedError } from "#generated/payment/paymentSchedule/PaymentScheduleAlreadyProcessedError"
import type { PaymentScheduleAlreadyRevokedError } from "#generated/payment/paymentSchedule/PaymentScheduleAlreadyRevokedError"
import type { PaymentScheduleNotFoundError } from "#generated/payment/paymentSchedule/PaymentScheduleNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type RevokePaymentSchedulesError =
	| BillingKeyAlreadyDeletedError
	| BillingKeyNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| PaymentScheduleAlreadyProcessedError
	| PaymentScheduleAlreadyRevokedError
	| PaymentScheduleNotFoundError
	| UnauthorizedError

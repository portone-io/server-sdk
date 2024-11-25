import type { Unrecognized } from "./../../../utils/unrecognized"
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
	| { readonly type: Unrecognized }

export function isUnrecognizedRevokePaymentSchedulesError(entity: RevokePaymentSchedulesError): entity is { readonly type: Unrecognized } {
	return entity.type !== "BILLING_KEY_ALREADY_DELETED"
		&& entity.type !== "BILLING_KEY_NOT_FOUND"
		&& entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PAYMENT_SCHEDULE_ALREADY_PROCESSED"
		&& entity.type !== "PAYMENT_SCHEDULE_ALREADY_REVOKED"
		&& entity.type !== "PAYMENT_SCHEDULE_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}

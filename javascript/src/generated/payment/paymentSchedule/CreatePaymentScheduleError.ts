import type { AlreadyPaidOrWaitingError } from "#generated/payment/paymentSchedule/AlreadyPaidOrWaitingError"
import type { BillingKeyAlreadyDeletedError } from "#generated/common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError } from "#generated/common/BillingKeyNotFoundError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PaymentScheduleAlreadyExistsError } from "#generated/common/PaymentScheduleAlreadyExistsError"
import type { SumOfPartsExceedsTotalAmountError } from "#generated/common/SumOfPartsExceedsTotalAmountError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type CreatePaymentScheduleError =
	| AlreadyPaidOrWaitingError
	| BillingKeyAlreadyDeletedError
	| BillingKeyNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| PaymentScheduleAlreadyExistsError
	| SumOfPartsExceedsTotalAmountError
	| UnauthorizedError

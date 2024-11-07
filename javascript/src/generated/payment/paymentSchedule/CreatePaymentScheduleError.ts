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

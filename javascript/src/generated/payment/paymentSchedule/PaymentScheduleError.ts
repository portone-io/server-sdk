import type { Unrecognized } from "../../../utils/unrecognized"
import { PaymentError } from "../PaymentError"
import type { AlreadyPaidOrWaitingError } from "../../payment/paymentSchedule/AlreadyPaidOrWaitingError"
import type { BillingKeyAlreadyDeletedError } from "../../common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError } from "../../common/BillingKeyNotFoundError"
import type { ForbiddenError } from "../../common/ForbiddenError"
import type { InvalidRequestError } from "../../common/InvalidRequestError"
import type { PaymentScheduleAlreadyExistsError } from "../../common/PaymentScheduleAlreadyExistsError"
import type { PaymentScheduleAlreadyProcessedError } from "../../payment/paymentSchedule/PaymentScheduleAlreadyProcessedError"
import type { PaymentScheduleAlreadyRevokedError } from "../../payment/paymentSchedule/PaymentScheduleAlreadyRevokedError"
import type { PaymentScheduleNotFoundError } from "../../payment/paymentSchedule/PaymentScheduleNotFoundError"
import type { SumOfPartsExceedsTotalAmountError } from "../../common/SumOfPartsExceedsTotalAmountError"
import type { UnauthorizedError } from "../../common/UnauthorizedError"
export abstract class PaymentScheduleError extends PaymentError {
	declare readonly data: AlreadyPaidOrWaitingError | BillingKeyAlreadyDeletedError | BillingKeyNotFoundError | ForbiddenError | InvalidRequestError | PaymentScheduleAlreadyExistsError | PaymentScheduleAlreadyProcessedError | PaymentScheduleAlreadyRevokedError | PaymentScheduleNotFoundError | SumOfPartsExceedsTotalAmountError | UnauthorizedError | { readonly type: Unrecognized }
}

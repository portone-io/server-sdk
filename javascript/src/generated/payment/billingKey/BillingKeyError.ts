import type { Unrecognized } from "../../../utils/unrecognized"
import { PaymentError } from "../PaymentError"
import type { BillingKeyAlreadyDeletedError } from "../../common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError } from "../../common/BillingKeyNotFoundError"
import type { BillingKeyNotIssuedError } from "../../payment/billingKey/BillingKeyNotIssuedError"
import type { ChannelNotFoundError } from "../../common/ChannelNotFoundError"
import type { ChannelSpecificError } from "../../payment/billingKey/ChannelSpecificError"
import type { ForbiddenError } from "../../common/ForbiddenError"
import type { InvalidRequestError } from "../../common/InvalidRequestError"
import type { PaymentScheduleAlreadyExistsError } from "../../common/PaymentScheduleAlreadyExistsError"
import type { PgProviderError } from "../../common/PgProviderError"
import type { UnauthorizedError } from "../../common/UnauthorizedError"
export abstract class BillingKeyError extends PaymentError {
	declare readonly data: BillingKeyAlreadyDeletedError | BillingKeyNotFoundError | BillingKeyNotIssuedError | ChannelNotFoundError | ChannelSpecificError | ForbiddenError | InvalidRequestError | PaymentScheduleAlreadyExistsError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
}

import type { BillingKeyAlreadyDeletedError } from "./../../common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError } from "./../../common/BillingKeyNotFoundError"
import type { BillingKeyNotIssuedError } from "./../../payment/billingKey/BillingKeyNotIssuedError"
import type { ChannelSpecificError } from "./../../payment/billingKey/ChannelSpecificError"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PaymentScheduleAlreadyExistsError } from "./../../common/PaymentScheduleAlreadyExistsError"
import type { PgProviderError } from "./../../common/PgProviderError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type DeleteBillingKeyError =
	| BillingKeyAlreadyDeletedError
	| BillingKeyNotFoundError
	| BillingKeyNotIssuedError
	| ChannelSpecificError
	| ForbiddenError
	| InvalidRequestError
	| PaymentScheduleAlreadyExistsError
	| PgProviderError
	| UnauthorizedError

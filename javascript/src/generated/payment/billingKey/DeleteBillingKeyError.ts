import type { BillingKeyAlreadyDeletedError } from "#generated/common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError } from "#generated/common/BillingKeyNotFoundError"
import type { BillingKeyNotIssuedError } from "#generated/payment/billingKey/BillingKeyNotIssuedError"
import type { ChannelSpecificError } from "#generated/payment/billingKey/ChannelSpecificError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PaymentScheduleAlreadyExistsError } from "#generated/common/PaymentScheduleAlreadyExistsError"
import type { PgProviderError } from "#generated/common/PgProviderError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

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

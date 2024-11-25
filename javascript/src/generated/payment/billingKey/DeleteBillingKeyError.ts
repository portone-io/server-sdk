import type { Unrecognized } from "./../../../utils/unrecognized"
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
	| { readonly type: Unrecognized }

export function isUnrecognizedDeleteBillingKeyError(entity: DeleteBillingKeyError): entity is { readonly type: Unrecognized } {
	return entity.type !== "BILLING_KEY_ALREADY_DELETED"
		&& entity.type !== "BILLING_KEY_NOT_FOUND"
		&& entity.type !== "BILLING_KEY_NOT_ISSUED"
		&& entity.type !== "CHANNEL_SPECIFIC"
		&& entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PAYMENT_SCHEDULE_ALREADY_EXISTS"
		&& entity.type !== "PG_PROVIDER"
		&& entity.type !== "UNAUTHORIZED"
}

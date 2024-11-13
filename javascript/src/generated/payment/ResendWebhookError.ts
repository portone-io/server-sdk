import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { MaxWebhookRetryCountReachedError } from "./../payment/MaxWebhookRetryCountReachedError"
import type { PaymentNotFoundError } from "./../payment/PaymentNotFoundError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
import type { WebhookNotFoundError } from "./../payment/WebhookNotFoundError"

export type ResendWebhookError =
	| ForbiddenError
	| InvalidRequestError
	| MaxWebhookRetryCountReachedError
	| PaymentNotFoundError
	| UnauthorizedError
	| WebhookNotFoundError
	| { readonly type: unique symbol }

import type { Unrecognized } from "./../../utils/unrecognized"
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
	| { readonly type: Unrecognized }

export function isUnrecognizedResendWebhookError(entity: ResendWebhookError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "MAX_WEBHOOK_RETRY_COUNT_REACHED"
		&& entity.type !== "PAYMENT_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
		&& entity.type !== "WEBHOOK_NOT_FOUND"
}

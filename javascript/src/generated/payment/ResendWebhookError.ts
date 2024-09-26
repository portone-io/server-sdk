import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PaymentNotFoundError } from "#generated/payment/PaymentNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"
import type { WebhookNotFoundError } from "#generated/payment/WebhookNotFoundError"

export type ResendWebhookError =
	| ForbiddenError
	| InvalidRequestError
	| PaymentNotFoundError
	| UnauthorizedError
	| WebhookNotFoundError

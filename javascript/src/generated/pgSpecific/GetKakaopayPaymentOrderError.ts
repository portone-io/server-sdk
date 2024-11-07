import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type GetKakaopayPaymentOrderError =
	| InvalidRequestError
	| UnauthorizedError

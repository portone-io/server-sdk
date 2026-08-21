import type { Unrecognized } from "../../utils/unrecognized"
import { RestError } from "../RestError"
import type { ForbiddenError } from "../common/ForbiddenError"
import type { InvalidRequestError } from "../common/InvalidRequestError"
import type { MaxTtlExceededError } from "../paymentSession/MaxTtlExceededError"
import type { SessionExpiredError } from "../paymentSession/SessionExpiredError"
import type { SessionNotFoundError } from "../paymentSession/SessionNotFoundError"
import type { UnauthorizedError } from "../common/UnauthorizedError"
export abstract class PaymentSessionError extends RestError {
	declare readonly data: ForbiddenError | InvalidRequestError | MaxTtlExceededError | SessionExpiredError | SessionNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
}

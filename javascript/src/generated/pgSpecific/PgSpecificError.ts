import type { Unrecognized } from "../../utils/unrecognized"
import { RestError } from "../RestError"
import type { InvalidRequestError } from "../common/InvalidRequestError"
import type { PaymentNotFoundError } from "../common/PaymentNotFoundError"
import type { UnauthorizedError } from "../common/UnauthorizedError"
export abstract class PgSpecificError extends RestError {
	declare readonly data: InvalidRequestError | PaymentNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
}

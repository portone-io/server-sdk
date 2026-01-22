import type { Unrecognized } from "../../utils/unrecognized"
import { RestError } from "../RestError"
import type { ForbiddenError } from "../common/ForbiddenError"
import type { InvalidRequestError } from "../common/InvalidRequestError"
import type { UnauthorizedError } from "../common/UnauthorizedError"
export abstract class ReconciliationError extends RestError {
	declare readonly data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
}
